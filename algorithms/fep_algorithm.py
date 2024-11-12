import numpy as np

class algorithm:
    def __init__(self, dim, pop_size, tournament_size, generations):
        self.dim = dim
        self.pop_size = pop_size
        self.tournament_size = tournament_size
        self.generations = generations

    def train(self, func):
        population = self.initialize_population()
        best_fitness_history = []
        best_fitness = float('inf')

        for generation in range(self.generations):
            offspring = [self.mutate(ind) for ind in population]
            combined_population = population + offspring
            fitness_values = self.evaluate_population(combined_population, func)
            population = self.tournament_selection(combined_population, fitness_values)

            generation_best = min(fitness_values)
            if generation_best < best_fitness:
                best_fitness = generation_best
            best_fitness_history.append(best_fitness)
            
        return best_fitness, best_fitness_history

    def initialize_population(self):
        return [(np.random.uniform(-5, 5, self.dim), np.random.uniform(0.1, 1.0, self.dim)) 
                for _ in range(self.pop_size)]

    def mutate(self, individual):
        x, sigma = individual
        tau = 1 / np.sqrt(2 * np.sqrt(len(x)))
        sigma_prime = sigma * np.exp(tau * np.random.normal(0, 1, len(x)))
        x_prime = x + sigma_prime * np.random.standard_cauchy(len(x))
        return x_prime, sigma_prime

    def evaluate_population(self, population, func):
        return [func(ind[0]) for ind in population]

    def tournament_selection(self, population, fitness):
        selected = []
        for _ in range(self.pop_size):
            indices = np.random.choice(len(population), min(self.tournament_size, len(population)), replace=False)
            selected.append(population[min(indices, key=lambda i: fitness[i])])
        return selected
