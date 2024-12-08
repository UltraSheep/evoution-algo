import numpy as np
from .. import config
from ..utils.evaluate_population import evaluate_population

c_rate = 0.80
m_rate = 0.20

class algorithm:    
    def __init__(self):
        self.name = "gen_elite algorithm"
        self.pop_size = config.POP_SIZE
        self.generations = config.GENERATIONS
        self.benchmark = config.BENCHMARK.function
        self.tournament_size = config.TOURNAMENT_SIZE
        self.params= config.BENCHMARK
        self.rs = np.random.RandomState(config.SEED)

    def train(self, initial_population):
        population = self.strip_sigma(initial_population)
        best_fitness_history = []
        best_fitness = float('inf')
        
        for generation in range(self.generations):
            global c_rate
            c_rate = 0.8 * (1 - generation / self.generations) + 0.4 * (generation / self.generations)
            global m_rate
            m_rate = 0.2 * (1 - generation / self.generations) + 0.01 * (generation / self.generations)
            population , best_fitness = self.evolve_elite (population)
            # 5 generations without improvement
            # 還沒用
            # best_fitness_streak = 0
            # previous_best_fitness = float('inf')
            # if abs(best_fitness - previous_best_fitness) < 1e-6:
            #     best_fitness_streak = best_fitness_streak + 1
            # else:
            #     best_fitness_streak = 0
            # previous_best_fitness = best_fitness

            # if best_fitness_streak >= 5:
            #     m_rate = min(m_rate * 1.5 , 0.5)
            #     c_rate = 0.9

            best_fitness_history.append (best_fitness)

        return best_fitness , best_fitness_history
            
    def strip_element_sigma(self, element):
        x, _ = element
        return x
    
    def strip_sigma(self, population):
        return [self.strip_element_sigma (ind) for ind in population]

    def elite_selection (self , pop , fitness):
        elite_count = max(1 , int(self.pop_size * 0.05))
        sorted_indices = np.argsort(fitness)
        elite_individuals = [pop[i] for i in sorted_indices[:elite_count]]
        elite_fitness = [fitness[i] for i in sorted_indices[:elite_count]]
        return elite_individuals, elite_fitness[0]

    def tournament_selection (self , n , pop , fitness):
        selected = []
        for i in range (n):
            # 2 pick 1
            # idx1 , idx2 = self.rs.choice (range(len(pop)), 2, replace = False)
            # if fitness[idx1] < fitness[idx2]:
            #     selected.append(pop[idx1])
            # else:
            #     selected.append(pop[idx2])

            # tournament_size pick 1
            candidates = self.rs.choice(range(len(pop)) , self.tournament_size , replace = False)
            best_idx = min (candidates , key = lambda idx: fitness[idx])
            selected.append(pop[best_idx])
        return selected

    def simulated_binary_crossover (self , parent1 , parent2 , eta = 0.5):
        child1 , child2 = np.copy(parent1) , np.copy(parent2)
        for i in range (len (parent1)):
            if self.rs.uniform(0 , 1) <= c_rate:
                u = self.rs.uniform(0 , 1)
                if u <= 0.5:
                    beta = (2 * u) ** (1 / (eta + 1))
                else:
                    beta = (1 / (2 * (1 - u))) ** (1 / (eta + 1))

                child1[i] = 0.5 * ((1 + beta) * parent1[i] + (1 - beta) * parent2[i])
                child2[i] = 0.5 * ((1 - beta) * parent1[i] + (1 + beta) * parent2[i])
        
            child1[i] = np.clip(child1[i], self.params.SMin , self.params.SMax)
            child2[i] = np.clip(child2[i], self.params.SMin , self.params.SMax)
        return child1 , child2

    def mutate (self , individual):
        for i in range (len (individual)):
            # print (m_rate)
            if self.rs.uniform (0 , 1) <= m_rate:
                individual[i] += self.rs.uniform (-1 , 1) * (self.params.SMax - self.params.SMin) * 0.1
                individual[i] = np.clip (individual[i] , self.params.SMin , self.params.SMax)
        return individual
    
    def evolve_elite (self , pop):
        fitness = evaluate_population(pop , self.benchmark)
        best_individuals , best_fitness = self.elite_selection (pop , fitness)

        new_population = best_individuals
        parents = self.tournament_selection (self.pop_size - 1 , pop , fitness)
        
        # Random selection 10% of the population
        # random_count = max(1, int(self.pop_size * 0.1))
        # random_indices = self.rs.choice(range(len(pop)) , random_count , replace=False)
        # random_individuals = [pop[i] for i in random_indices]
        # new_population = best_individuals + random_individuals
        # parents = self.tournament_selection(self.pop_size - len(new_population) , pop , fitness)

        for i in range (0 , len (parents) , 2):
            parent1 , parent2 = parents[i] , parents[min (i + 1 , len (parents) - 1)]
            child1 , child2 = self.simulated_binary_crossover (parent1 , parent2)
            new_population.append (self.mutate (child1))
            if len (new_population) < self.pop_size:
                new_population.append (self.mutate (child2))

        return new_population, best_fitness
