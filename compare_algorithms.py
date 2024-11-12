import numpy as np
import matplotlib.pyplot as plt
import importlib
import os

from benchmark_functions import sphere as benchmark # Modify this to change benchmark function

# Parameters
DIM = 5
GENERATIONS = 100
POP_SIZE = 50

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

for module in algorithms:
    algorithm = module.algorithm(POP_SIZE, GENERATIONS, benchmark)
    best_fitness, best_fitness_history = algorithm.train(initialize_population())
    plt.plot(best_fitness_history, label=f"{algorithm.name.capitalize()}")
    print(f"{algorithm.name.capitalize()} - Best Fitness: {best_fitness}")
    
print(f"Best Theoretical Fitness: {benchmark.FMin}")

plt.xlabel("Generation")
plt.ylabel("Best Fitness")
plt.title(f"Algorithm Performance Comparison\nBest Theoretical Fitness: {benchmark.FMin}")
plt.legend()
plt.grid(True)
plt.show()