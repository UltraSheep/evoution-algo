import numpy as np
import matplotlib.pyplot as plt
import importlib
import os
import threading
import config

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
def initialize_population():
    #np.random.seed(config.SEED)
    return [
        (np.random.uniform(config.BENCHMARK.SMin, config.BENCHMARK.SMax, config.DIM), 
            np.random.uniform(0.1, 1.0, config.DIM))
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
algorithms = import_algorithms("./algorithms")
initial_populations = [initialize_population() for _ in range(config.RUNS)]

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

with open(config.RESULTS_FILE, "w") as file:
    file.write("Benchmark function = "+ config.BENCHMARK.__name__)
    file.write(f"\nDimension = {config.DIM}\nGenerations = {config.GENERATIONS}\nPopulation size = {config.DIM}\nRuns = {config.RUNS}\nSeed = {config.SEED}\n")
    file.write("\n".join(summary))
    file.write(f"Best Theoretical Fitness: {config.BENCHMARK.FMin}")

print(f"Best Theoretical Fitness: {config.BENCHMARK.FMin}")
plt.xlabel("Generation")
plt.ylabel("Best Fitness")
plt.title(f"Algorithm Average Performance Comparison\nBest Theoretical Fitness: {config.BENCHMARK.FMin}")
plt.legend()
plt.grid(True)
plt.show()