from pydantic import BaseModel, Field
import numpy.random as np

class INDIVIDUAL(BaseModel):
    id:int
    health:int = None
    weapon:int = None
    speed:int = None
    jump:int = None
    def initialize(self):
        self.health = np.randint(100)
        self.weapon = np.randint(100)
        self.speed  = np.randint(100)
        self.jump   = np.randint(100)
    def denormalize(self):
        self.health = int (self.health * 0.4 + 1)
        self.weapon = int (self.weapon * 0.03)
        self.speed  = int (self.speed * 0.5 + 50)
        self.jump   = int (self.jump * 3 + 100)

class LEVEL(BaseModel):
    enemies: list[INDIVIDUAL] = None
    def denormalize(self):
        for individual in self.enemies:
            individual.denormalize()

class POPULATION(BaseModel):
    pop: list[LEVEL] = None
    def denormalize(self):
        for level in self.pop:
            level.denormalize()

class RESULT(BaseModel):
    fitness:list[int]