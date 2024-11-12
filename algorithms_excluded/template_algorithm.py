import numpy as np
from evaluate_population import evaluate_population

# other parameters

class algorithm:    
    def __init__(self, pop_size, tournament_size, generations, benchmark):
        self.name = "example algorithm"
        self.pop_size = pop_size
        self.tournament_size = tournament_size
        self.generations = generations
        self.benchmark = benchmark.function
        self.params=benchmark

    def train(self, initial_population):
        population = initial_population
        best_fitness_history = []
        best_fitness = float('inf')
        for generation in range(self.generations):

            # algorithm here

            fitness_values = evaluate_population(population, self.benchmark)
            generation_best = min(fitness_values)
            if generation_best < best_fitness:
                best_fitness = generation_best
            best_fitness_history.append(best_fitness)

        return best_fitness, best_fitness_history
    
    # [self.strip_sigma(ind) for ind in population]
    def strip_sigma(self, element):
        x,sigma = element
        return x