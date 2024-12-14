from .structures import INDIVIDUAL, LEVEL, POPULATION
from .. import config

def initialize_population ():
    levels = []
    population = POPULATION()
    for i in range (config.POP_SIZE):
        individuals = []
        for i in range (config.ENEMY_COUNT):
            individual = INDIVIDUAL(id = i)
            individual.initialize()
            individuals.append (individual)
        levels.append(LEVEL(enemies = individuals))
    population.pop = levels
    return population