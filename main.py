from fastapi import FastAPI
from .algorithms.gen_2n_n import algorithm
from .utils.initialize_environment import initialize_environment
from .utils.initialize_population import initialize_population
from .utils.structures import POPULATION, RESULT

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
    current_population.pop = algorithm.train(current_population.pop, result.fitness)
    return {"population": current_population.pop}