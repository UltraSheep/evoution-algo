from fastapi import FastAPI
from .algorithms.gen_2n_n import train
from .utils.initialize_environment import initialize_environment
from .utils.initialize_population import initialize_population
from .utils.structures import POPULATION, RESULT

current_population = POPULATION()
initialize_environment()

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
    current_population = initialize_population()
    denormalized_population = current_population
    denormalized_population.denormalize()
    return {"population" : denormalized_population.pop}

@app.put("/next_generation")
async def next_generation(result : RESULT):
    current_population.pop = train(current_population.pop , result.fitness)
    denormalized_population = current_population
    denormalized_population.denormalize()
    return {"population" : denormalized_population.pop}