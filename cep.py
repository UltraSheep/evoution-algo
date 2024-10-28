import numpy as np
from benchmark_functions import sphere as target  # Replace with desired function

# Parameters
POP_SIZE = 50
TOURNAMENT_SIZE = 10
GENERATIONS = 100
DIMENSIONS = 5

def initialize_population(dim, pop_size=POP_SIZE):
    return [(np.random.uniform(-5, 5, dim), np.random.uniform(0.1, 1.0, dim)) for _ in range(pop_size)]

def gaussian_mutation(individual):
    x, sigma = individual
    tau = 1 / np.sqrt(2 * np.sqrt(len(x)))
    sigma_prime = sigma * np.exp(tau * np.random.normal(0, 1, len(x)))
    x_prime = x + sigma_prime * np.random.normal(0, 1, len(x))
    return x_prime, sigma_prime

def evaluate_population(population, func):
    return [func(ind[0]) for ind in population]

def tournament_selection(population, fitness, size=TOURNAMENT_SIZE, target_size=POP_SIZE):
    selected = []
    for _ in range(target_size):
        indices = np.random.choice(len(population), min(size, len(population)), replace=False)
        selected.append(population[min(indices, key=lambda i: fitness[i])])
    return selected

def cep_algorithm(func, dim, generations=GENERATIONS):
    population = initialize_population(dim)
    best_solution, best_fitness = None, float('inf')

    for generation in range(generations):
        print(f"\nGeneration {generation + 1}/{generations}")
        
        offspring = [gaussian_mutation(ind) for ind in population]
        combined_population = population + offspring
        fitness_values = evaluate_population(combined_population, func)
        
        population = tournament_selection(combined_population, fitness_values)
        
        generation_best = min(fitness_values)
        if generation_best < best_fitness:
            best_fitness = generation_best
            best_solution = combined_population[fitness_values.index(generation_best)][0]
        
        print(f"Best fitness this generation: {generation_best:.4f}")
        print(f"Overall best fitness: {best_fitness:.4f}")

    return best_solution, best_fitness

if __name__ == "__main__":
    best_sol, best_fit = cep_algorithm(target, DIMENSIONS)
    print("\nBest Solution Found:", best_sol)
    print("Best Fitness Achieved:", best_fit)
