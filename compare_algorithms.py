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

algorithms = import_algorithms('evoution-algo/algorithms')

def run_algorithm(algorithm_class, func):
    algorithm = algorithm_class(DIM, POP_SIZE, TOURNAMENT_SIZE)
    population = algorithm.initialize_population()
    best_fitness_history = []
    best_fitness = float('inf')
    
    for generation in range(GENERATIONS):
        offspring = [algorithm.mutate(ind) for ind in population]
        combined_population = population + offspring
        fitness_values = algorithm.evaluate_population(combined_population, func)
        population = algorithm.tournament_selection(combined_population, fitness_values)
        
        generation_best = min(fitness_values)
        if generation_best < best_fitness:
            best_fitness = generation_best
        best_fitness_history.append(best_fitness)
        
    return best_fitness, best_fitness_history

for algorithm_name, module in algorithms.items():
    algorithm_class = module.algorithm
    best_fit, fitness_history = run_algorithm(algorithm_class, current_function)

    plt.plot(fitness_history, label=f"{algorithm_name.capitalize()}")
    print(f"{algorithm_name.capitalize()} - Best Fitness: {best_fit}")

plt.xlabel("Generation")
plt.ylabel("Best Fitness")
plt.title("Algorithm Performance Comparison")
plt.legend()
plt.grid(True)
plt.show()