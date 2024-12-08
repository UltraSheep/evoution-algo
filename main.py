from fastapi import FastAPI
from pydantic import BaseModel

class INDIVIDUAL(BaseModel):
    id:int
    health:int
    weapon:int
    speed:int
    jump:int

class POPULATION(BaseModel):
    pop: list[INDIVIDUAL]

class RESULT(BaseModel):
    fitness:list[int]

current_population = POPULATION()
initialize_environment()

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/initialize")
async def initialize():
    current_population = POPULATION()
    current_population.pop = initialize_population()
    return {"population": current_population.pop}

@app.put("/next_generation")
async def next_generation(result:RESULT):
    current_population.pop = train(current_population.pop, result.fitness)
    return {"population": current_population.pop}