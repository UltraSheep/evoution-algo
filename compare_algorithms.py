# compare_algorithms.py
import numpy as np
import matplotlib.pyplot as plt
from benchmark_functions import sphere as current_function  # Replace with your desired benchmark function
from cep_algorithm import CEPAlgorithm
from fep_algorithm import FEPAlgorithm

def run_algorithm(algorithm_class, func, dim, generations=100):
    algorithm = algorithm_class(dim)
    population = algorithm.initialize_population()
    best_fitness_history = []
    best_fitness = float('inf')
    
    for generation in range(generations):
        offspring = [algorithm.mutate(ind) for ind in population]
        combined_population = population + offspring
        fitness_values = algorithm.evaluate_population(combined_population, func)
        population = algorithm.tournament_selection(combined_population, fitness_values)
        
        generation_best = min(fitness_values)
        if generation_best < best_fitness:
            best_fitness = generation_best
        best_fitness_history.append(best_fitness)
        
    return best_fitness, best_fitness_history

# Parameters
DIM = 5
GENERATIONS = 100

# Run CEP and FEP
best_fit_cep, fitness_history_cep = run_algorithm(CEPAlgorithm, current_function, DIM, GENERATIONS)
best_fit_fep, fitness_history_fep = run_algorithm(FEPAlgorithm, current_function, DIM, GENERATIONS)

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(fitness_history_cep, label="CEP Algorithm")
plt.plot(fitness_history_fep, label="FEP Algorithm")
plt.xlabel("Generation")
plt.ylabel("Best Fitness")
plt.title("CEP vs FEP Algorithm Performance")
plt.legend()
plt.grid(True)
plt.show()

# Output best results
print("CEP Algorithm - Best Fitness:", best_fit_cep)
print("FEP Algorithm - Best Fitness:", best_fit_fep)
