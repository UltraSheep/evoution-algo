import numpy as np
import matplotlib.pyplot as plt
import importlib
import os

from benchmark_functions import schwefel_2_22 as benchmark # Modify this to change benchmark function

# Parameters
DIM = 5
GENERATIONS = 100
POP_SIZE = 50
RUNS = 10

def import_algorithms(folder):
    algorithms = []
    for filename in os.listdir(folder):
        if filename.endswith('.py') and filename != '__init__.py' and filename != 'evaluate.pya':
            module_name = filename[:-3]
            module = importlib.import_module(f'algorithms.{module_name}')
            algorithms.append(module)
    return algorithms

def initialize_population():
    return [(np.random.uniform(benchmark.SMax, benchmark.SMin, DIM), np.random.uniform(0.1, 1.0, DIM)) 
                for _ in range(POP_SIZE)]

algorithms = import_algorithms('./algorithms')

initial_populations = []
for run in range(RUNS) :
    initial_populations.append(initialize_population())

for module in algorithms:
    best_fitness_history_per_run = []
    best_fitness_per_run = []

    for run in range(RUNS) :
        algorithm = module.algorithm(POP_SIZE, GENERATIONS, benchmark)
        best_fitness, best_fitness_history = algorithm.train(initial_populations[run])

        best_fitness_per_run.append(best_fitness)
        best_fitness_history_per_run.append(best_fitness_history)

    print(f"{algorithm.name.capitalize()} - Average Best Fitness: {np.average(best_fitness_per_run)}")
    print(f"{algorithm.name.capitalize()} - Standard Deviation: {np.std(best_fitness_per_run)}")
    plt.plot(np.mean(best_fitness_history_per_run, axis=0), label=f"{algorithm.name.capitalize()}")
    
print(f"Best Theoretical Fitness: {benchmark.FMin}")
plt.xlabel("Generation")
plt.ylabel("Best Fitness")
plt.title(f"Algorithm Average Performance Comparison\nBest Theoretical Fitness: {benchmark.FMin}")
plt.legend()
plt.grid(True)
plt.show()