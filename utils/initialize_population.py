from .. import config
from .structures import INDIVIDUAL 
import numpy.random as np


def initialize_population ():
    population = []
    for i in range (config.POP_SIZE):
        individual = INDIVIDUAL(id = i , health = np.randint(1 , 40) , weapon = np.randint(1 , 3) , speed = np.randint(50 , 100) , jump = np.randint(100 , 400))
        population.append (individual)

    return population