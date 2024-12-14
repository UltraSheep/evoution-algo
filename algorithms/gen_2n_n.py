import numpy as np
from .. import config
from ..utils.structures import *

c_rate = 0.80
m_rate = 0.20

pre_fitness = None  # Declare fitness as a global variable

class algorithm:    
    def __init__(self):
        self.name = "gen_2n_n algorithm"
        self.pop_size = config.POP_SIZE
        self.tournament_size = config.TOURNAMENT_SIZE
        self.SMax = config.SMAX
        self.SMin = config.SMIN
        self.rs = np.random.RandomState(config.SEED)

    def strip_element_sigma (self , element):
        x , _ = element
        return x
    
    def strip_sigma (self , population):
        return [self.strip_element_sigma(ind) for ind in population]

    def elite_selection (self , pop , fitness):
        elite_count = max(1 , int(self.pop_size * 0.05))
        sorted_indices = np.argsort(fitness)
        elite_individuals = [pop[i] for i in sorted_indices[:elite_count]]
        elite_fitness = [fitness[i] for i in sorted_indices[:elite_count]]
        return elite_individuals , elite_fitness[0]

    def tournament_selection (self , pop , fitness):
        selected = []
        for i in range(self.pop_size):
            candidates = self.rs.choice (range(len(pop)) , self.tournament_size , replace = False)
            best_idx = min(candidates , key = lambda idx: fitness[idx])
            selected.append (pop[best_idx])
        return selected

    def simulated_binary_crossover (self , parent1 , parent2 , eta = 0.5):
        child1 , child2 = np.copy (parent1) , np.copy (parent2)
        for i in range (len(parent1)):
            if self.rs.uniform (0 , 1) <= c_rate:
                u = self.rs.uniform (0 , 1)
                if u <= 0.5:
                    beta = (2 * u) ** (1 / (eta + 1))
                else:
                    beta = (1 / (2 * (1 - u))) ** (1 / (eta + 1))

                child1[i] = 0.5 * ((1 + beta) * parent1[i] + (1 - beta) * parent2[i])
                child2[i] = 0.5 * ((1 - beta) * parent1[i] + (1 + beta) * parent2[i])
        
            child1[i] = np.clip(child1[i] , self.SMin, self.SMax)
            child2[i] = np.clip(child2[i] , self.SMin, self.SMax)

        return child1 , child2

    def mutate (self , individual):
        for i in range (len(individual)):
            if self.rs.uniform (0 , 1) <=m_rate:
                individual[i] += self.rs.uniform (-1 , 1) * (self.SMax - self.SMin) * 0.1
                individual[i] = np.clip (individual[i] , self.SMin , self.SMax)
        return individual

    def evolve(self , pop , parents):
        offspring = []
        for i in range (0 , len(parents) , 2):
            parent1 , parent2 = parents[i] , parents[min(i + 1 , len(parents) - 1)]
            child1  , child2  = self.simulated_binary_crossover (parent1 , parent2)
            offspring.append (self.mutate(child1))
            if len(offspring) < self.pop_size:
                offspring.append (self.mutate(child2))

        combined_population = pop + offspring
        return combined_population , offspring
    
    def evolve_c_2n_n (self , pop , curr_fitness):
        global pre_fitness
        offspring = []

        if pre_fitness is None:
            combined_population , offspring = self.evolve (pop , pop)
            pre_fitness = curr_fitness
            # Debug output
            # print("Initial pre_fitness:" , pre_fitness)
            return offspring , pre_fitness[0]

        parents = self.tournament_selection (pop , pre_fitness)
        combined_population , _ = self.evolve (pop , parents)

        combined_fitness = pre_fitness + curr_fitness
        sorted_indices = np.argsort (combined_fitness)

        combined_population = np.array(combined_population , dtype = object)
        new_population = [combined_population[i] for i in sorted_indices[:self.pop_size]]
       
        # update global fitness
        pre_fitness = [combined_fitness[i] for i in sorted_indices[:self.pop_size]]

        # Debug output
        print ("combined_fitness: " , combined_fitness)
        print ("sorted_indices: "   , sorted_indices)
        print ("new_population: "   , new_population)
        print ("pre_fitness: "      , pre_fitness)

        return new_population , pre_fitness[0]

algo = algorithm()

def train (population_data: POPULATION , fitness_data: RESULT):
    population = population_data.flatten()
    fitness = fitness_data.fitness
    # Debug output
    # print ("in train population:" + population)

    new_population_data , _ = algo.evolve_c_2n_n (population , fitness)

    new_population = []
        
    for i in range (algo.pop_size):
        each_new_population_data = []
        for j in range (config.ENEMY_COUNT):
            base_index = i * config.DIM + j * config.ENEMY_PARAMS
            one_enemy = [INDIVIDUAL (id = j,
                                     health = new_population_data[base_index + 0],
                                     weapon = new_population_data[base_index + 1],
                                     speed  = new_population_data[base_index + 2],
                                     jump   = new_population_data[base_index + 3])]
            each_new_population_data.append(one_enemy)
        new_population.append(each_new_population_data)


    # for i , data in enumerate (each_new_population_data):
    #     new_population.append (INDIVIDUAL ( id = i ,
    #                                         health = data[0] ,
    #                                         weapon = data[1] ,
    #                                         speed  = data[2] ,
    #                                         jump   = data[3]))
    
    # Debug output
    # print("in train new_population:")
    # print(new_population)
    return new_population