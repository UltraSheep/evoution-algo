import numpy as np
import matplotlib.pyplot as plt
import importlib
import os
import datetime
import threading
import config
from nicegui import ui

from pathlib import Path

# Imports algorithm modules from the specified folder.
def import_algorithms(folder):
    algorithms = []
    for filename in os.listdir(folder):
        if filename.endswith('.py') and filename not in ['__init__.py']:
            module_name = filename[:-3]
            try:
                module = importlib.import_module(f'algorithms.{module_name}')
                if hasattr(module, 'algorithm'):
                    algorithms.append(module)
                else:
                    print(f"Warning: '{module_name}' lacks an 'algorithm' class or function.")
            except ImportError as e:
                print(f"Error importing {module_name}: {e}")
    return algorithms

# Initializes a population
def initialize_population(rs):
    return [
        (rs.uniform(config.BENCHMARK.SMin, config.BENCHMARK.SMax, config.DIM), 
            rs.uniform(0.1, 1.0, config.DIM))
        for _ in range(config.POP_SIZE)
    ]

# Runs each algorithm in a separate thread and records results.
def run_algorithm(algorithm, initial_population, results):
    best_fitness_history_per_run = []
    best_fitness_per_run = []
    algo_instance = algorithm.algorithm()
    for run in range(config.RUNS):
        best_fitness, best_fitness_history = algo_instance.train(initial_population[run])
        best_fitness_per_run.append(best_fitness)
        best_fitness_history_per_run.append(best_fitness_history)

    results[algo_instance.name] = {
        "average_best_fitness": np.mean(best_fitness_per_run),
        "std_dev": np.std(best_fitness_per_run),
        "fitness_history": np.mean(best_fitness_history_per_run, axis=0)
    }

# Start
def start():
    rs = np.random.RandomState(config.SEED)
    algorithms = import_algorithms("./algorithms")
    initial_populations = [initialize_population(rs) for _ in range(config.RUNS)]

    threads = []
    results = {}
    for module in algorithms:
        thread = threading.Thread(target=run_algorithm, args=(module, initial_populations, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    summary = []
    for name, result in results.items():
        output = f"{name.capitalize()} - Avg Best Fitness: {result['average_best_fitness']}, Std Dev: {result['std_dev']}"
        print(output)
        summary.append(output)
        plt.plot(result["fitness_history"], label=f"{name.capitalize()}")

    Path("./results").mkdir(exist_ok=True)
    with open(f"./results/{config.RESULTS_FILE}_{datetime.datetime.now().strftime('%Y_%m_%d_%H%M%S')}.txt", "w") as file:
        file.write("Benchmark function = "+ config.BENCHMARK.__name__)
        file.write(f"\nDimension = {config.DIM}\nGenerations = {config.GENERATIONS}\nPopulation size = {config.POP_SIZE}\nRuns = {config.RUNS}\nSeed = {config.SEED}\nTournament size = {config.TOURNAMENT_SIZE}\n")
        file.write("\n".join(summary))
        file.write(f"\nBest Theoretical Fitness: {config.BENCHMARK.FMin}")

    print(f"Best Theoretical Fitness: {config.BENCHMARK.FMin}")

    if config.PLOT:
        plt.xlabel("Generation")
        plt.ylabel("Best Fitness")
        plt.title(f"Algorithm Average Performance Comparison\nBest Theoretical Fitness: {config.BENCHMARK.FMin}")
        plt.legend()
        plt.grid(True)
        plt.show()
    return file.name