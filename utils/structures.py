from pydantic import BaseModel
import numpy.random as random
from .. import config

def rng():
    return random.randint(config.SMIN, config.SMAX)

class INDIVIDUAL(BaseModel):
    id:     int = None
    health: int = None
    weapon: int = None
    speed:  int = None
    jump:   int = None

    def initialize(self):
        self.health = rng()
        self.weapon = rng()
        self.speed  = rng()
        self.jump   = rng()

    def _denormalize(self):
        self.health = int (self.health * 0.4 + 1)
        self.weapon = int (self.weapon * 0.03)
        self.speed  = int (self.speed * 0.5 + 50)
        self.jump   = int (self.jump * 3 + 100)

class LEVEL(BaseModel):
    score: int = None
    enemies: list[INDIVIDUAL] = None

    def _denormalize(self):
        for individual in self.enemies:
            individual._denormalize()

class POPULATION(BaseModel):
    id: int = None
    pop: list[LEVEL] = None

    def flatten(self):
        result = []
        for level in self.pop:
            flattened = []
            for enemy in level.enemies:
                flattened.append(enemy.health)
                flattened.append(enemy.weapon)
                flattened.append(enemy.speed)
                flattened.append(enemy.jump)
            result.append(flattened)
        return result
    
    def denormalize(self):
        for level in self.pop:
            level._denormalize()

class RESULT(BaseModel):
    fitness: list[int]

class LOG(BaseModel):
    population_size: int
    tournament_size: int
    enemies_per_level: int
    generations: list[POPULATION] = None