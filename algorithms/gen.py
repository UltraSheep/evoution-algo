import numpy as np
import config

import random
from utils.evaluate_population import evaluate_population

c_rate = 0.70
m_rate = 0.01

class algorithm:    
    def __init__(self):
        self.name = "gen algorithm"
        self.pop_size = config.POP_SIZE
        self.generations = config.GENERATIONS
        self.benchmark = config.BENCHMARK.function
        self.params= config.BENCHMARK

    def train(self, initial_population):
        population = self.strip_sigma(initial_population)
        best_fitness_history = []
        best_fitness = float('inf')
        
        for _ in range(self.generations):
            population , best_fitness = self.evolve (population)
            best_fitness_history.append (best_fitness)

        return best_fitness , best_fitness_history
            
        # algorithm here
        #fitness_values = evaluate_population(population, self.benchmark)

    def strip_element_sigma(self, element):
        x, _ = element
        return x
    
    def strip_sigma(self, population):
        return [self.strip_element_sigma(ind) for ind in population]

    def elite_selection (self , pop , fitness):
        best_index = np.argmin(fitness)
        return pop[best_index] , fitness[best_index]

    def tournament_selection (self , n , pop , fitness):
        selected = []
        for i in range(n):
            idx1 , idx2 = random.sample(range (len(pop)) , 2)
            if fitness[idx1] < fitness[idx2]:
                selected.append(pop[idx1])
            else:
                selected.append(pop[idx2])
        return selected

    def simulated_binary_crossover (self , parent1 , parent2 , eta = 2):
        child1 , child2 = np.copy(parent1) , np.copy(parent2)
        for i in range (len (parent1)):
            if random.uniform(0, 1) <= c_rate:
                u = random.uniform(0, 1)
                if u <= 0.5:
                    beta = (2 * u) ** (1 / (eta + 1))
                else:
                    beta = (1 / (2 * (1 - u))) ** (1 / (eta + 1))
                child1[i] = 0.5 * ((1 + beta) * parent1[i] + (1 - beta) * parent2[i])
                child2[i] = 0.5 * ((1 - beta) * parent1[i] + (1 + beta) * parent2[i])
        return child1 , child2

    def mutate (self , individual):
        for i in range (len (individual)):
            if random.uniform (0 , 1) <= m_rate:
                individual[i] += random.uniform (-1 , 1) * (self.params.SMax - self.params.SMin) * 0.1
                individual[i] = np.clip (individual[i] , self.params.SMin , self.params.SMax)
        return individual
    
    def evolve (self , pop):
        fitness = evaluate_population(pop , self.benchmark)
        best_individual , best_fitness = self.elite_selection (pop , fitness)

        new_population = [best_individual]
        parents = self.tournament_selection (self.pop_size - 1 , pop , fitness)

        for i in range (0 , len (parents) , 2):
            parent1, parent2 = parents[i] , parents[min (i + 1 , len (parents) - 1)]
            child1, child2 = self.simulated_binary_crossover (parent1 , parent2)
            new_population.append (self.mutate (child1))
            if len (new_population) < self.pop_size:
                new_population.append (self.mutate (child2))

        return new_population, best_fitness