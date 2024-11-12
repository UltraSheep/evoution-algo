import numpy as np
from evaluate_population import evaluate_population

class algorithm:    
    def __init__(self, pop_size, tournament_size, generations, benchmark):
        self.name = "example algorithm"
        self.pop_size = pop_size
        self.tournament_size = tournament_size
        self.generations = generations
        self.benchmark = benchmark

    def train(self, initial_population):
        population = initial_population
        best_fitness_history = []
        best_fitness = float('inf')
        
        # algorithm here
        #fitness_values = evaluate_population(population, self.benchmark)


        return best_fitness, best_fitness_history

