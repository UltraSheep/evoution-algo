from pydantic import BaseModel

class INDIVIDUAL(BaseModel):
    id:int
    health:int
    weapon:int
    speed:int
    jump:int

class POPULATION(BaseModel):
    pop: list[INDIVIDUAL]= None

class RESULT(BaseModel):
    fitness:list[int]