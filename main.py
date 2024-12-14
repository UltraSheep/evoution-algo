import copy

from fastapi import FastAPI

from .utils import *
from .config import train

current_population = None
generation = None
app = FastAPI()

@app.get("/initialize")
async def initialize():
    initialize_environment()
    global current_population, generation
    generation = 0
    current_population = initialize_population()
    denormalized_population = copy.deepcopy(current_population)
    denormalized_population.denormalize()
    return {"population" : denormalized_population.pop}

@app.put("/next_generation")
async def next_generation(result : RESULT):
    global current_population, generation
    log(generation, current_population, result)
    generation += 1
    current_population.pop = train(current_population , result)
    denormalized_population = copy.deepcopy(current_population)
    denormalized_population.denormalize()
    return {"population" : denormalized_population.pop}