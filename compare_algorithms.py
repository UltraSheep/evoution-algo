import numpy as np
import matplotlib.pyplot as plt
import importlib
import os

from benchmark_functions import sphere as current_function # Modify this to change benchmark function

# Parameters
DIM = 5
GENERATIONS = 100
POP_SIZE = 50
TOURNAMENT_SIZE = 10

def import_algorithms(folder):
    algorithms = {}
    for filename in os.listdir(folder):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]
            module = importlib.import_module(f'algorithms.{module_name}')
            algorithms[module_name] = module
    return algorithms

algorithms = import_algorithms('./algorithms')

for algorithm_name, module in algorithms.items():
    algorithm = module.algorithm(DIM, POP_SIZE, TOURNAMENT_SIZE, GENERATIONS)
    best_fitness, best_fitness_history = algorithm.train(current_function)
    plt.plot(best_fitness_history, label=f"{algorithm_name.capitalize()}")
    print(f"{algorithm_name.capitalize()} - Best Fitness: {best_fitness}")

plt.xlabel("Generation")
plt.ylabel("Best Fitness")
plt.title("Algorithm Performance Comparison")
plt.legend()
plt.grid(True)
plt.show()