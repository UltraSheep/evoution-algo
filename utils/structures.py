from pydantic import BaseModel
import numpy.random as np

class INDIVIDUAL(BaseModel):
    id:int     = None
    health:int = None
    weapon:int = None
    speed:int  = None
    jump:int   = None

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

    def flatten(self):
        flattened = []
        for level in self.pop:
            for enemy in level.enemies:
                flattened.append(enemy.health)
                flattened.append(enemy.weapon)
                flattened.append(enemy.speed)
                flattened.append(enemy.jump)
        return flattened
    
    def denormalize(self):
        for level in self.pop:
            level.denormalize()

class RESULT(BaseModel):
    fitness:list[int]