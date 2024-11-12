import numpy as np
from evaluate_population import evaluate_population

tournament_size = 10

class algorithm:    
    def __init__(self, pop_size, generations, benchmark):
        self.name = "fep algorithm"
        self.pop_size = pop_size
        self.generations = generations
        self.benchmark = benchmark.function
        self.params=benchmark

    def train(self, initial_population):
        population = initial_population
        best_fitness_history = []
        best_fitness = float('inf')

        for generation in range(self.generations):
            offspring = [self.mutate(ind) for ind in population]
            combined_population = population + offspring
            fitness_values = evaluate_population(self.strip_sigma(combined_population), self.benchmark)
            population = self.tournament_selection(combined_population, fitness_values)

            generation_best = min(fitness_values)
            if generation_best < best_fitness:
                best_fitness = generation_best
            best_fitness_history.append(best_fitness)

        return best_fitness, best_fitness_history
    
    def strip_element_sigma(self, element):
        x,sigma = element
        return x
    
    def strip_sigma(self, population):
        return [self.strip_element_sigma(ind) for ind in population]

    def mutate(self, individual):
        x, sigma = individual
        tau = 1 / np.sqrt(2 * np.sqrt(len(x)))
        sigma_prime = sigma * np.exp(tau * np.random.normal(0, 1, len(x)))
        x_prime = x + sigma_prime * np.random.standard_cauchy(len(x))
        return x_prime, sigma_prime

    def tournament_selection(self, population, fitness):
        selected = []
        for _ in range(self.pop_size):
            indices = np.random.choice(len(population), min(tournament_size, len(population)), replace=False)
            selected.append(population[min(indices, key=lambda i: fitness[i])])
        return selected

