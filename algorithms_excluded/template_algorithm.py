import numpy as np
import config
from utils.evaluate_population import evaluate_population

# other parameters

class algorithm:    
    def __init__(self):
        self.name = "example algorithm"
        self.pop_size = config.POP_SIZE
        self.generations = config.GENERATIONS
        self.benchmark = config.BENCHMARK.function
        self.params= config.BENCHMARK
        self.tournament_size = config.TOURNAMENT_SIZE
        self.rs = np.random.RandomState(config.SEED)

    def train(self, initial_population):
        # for algorithms that dont use sigma, replace with this:
        # population = self.strip_sigma(initial_population)
        population = initial_population
        best_fitness_history = []
        best_fitness = float('inf')
        for _ in range(self.generations):

            # algorithm here
            # use self.rs instead of np.random

            # for algorithms that dont use sigma, replace with this:
            # fitness_values = evaluate_population(population, self.benchmark)
            fitness_values = evaluate_population(self.strip_sigma(population), self.benchmark)
            generation_best = min(fitness_values)
            if generation_best < best_fitness:
                best_fitness = generation_best
            best_fitness_history.append(best_fitness)

        return best_fitness, best_fitness_history
    
    def strip_element_sigma(self, element):
        x, _ = element
        return x
    
    def strip_sigma(self, population):
        return [self.strip_element_sigma(ind) for ind in population]