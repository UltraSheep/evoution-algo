from .. import config
from .structures import INDIVIDUAL 

def initialize_population ():
    population = []
    for i in range (config.POP_SIZE):
        individual = INDIVIDUAL(id = i , health = 10 , weapon = 50 , speed = 30 , jump = 20)
        population.append (individual)

    return population