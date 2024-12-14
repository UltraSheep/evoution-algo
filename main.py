import copy
from fastapi import FastAPI
from .config import train
from .utils.initialize_environment import initialize_environment
from .utils.initialize_population import initialize_population
from .utils.log_results import log
from .utils.structures import RESULT

current_population = None
generation = None
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.put("/console-log")
async def consolelog (result : RESULT):
    print(result)
    return {"message" : "success"}

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
    current_population.pop = train(current_population , result.fitness)
    denormalized_population = copy.deepcopy(current_population)
    denormalized_population.denormalize()
    return {"population" : denormalized_population.pop}