from fastapi import FastAPI
from ..compare_algorithms import run_test, init
import pkgutil
from pydantic import BaseModel

class individual(BaseModel):
    id:int
    health:int
    weapon:int
    speed:int
    jump:int

class population(BaseModel):
    population: list[individual]

class result(BaseModel):
    fitness:list[int]

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/run")
async def run():
    result_file = run_test()
    return {"result file":result_file }


@app.get("/list-modules")
async def list_modules():
    modules = [module.name for module in pkgutil.iter_modules()]
    return {"modules": modules}


@app.post("/init")
async def initialize():
    return {"initial_population": init()}

@app.put("/result")
async def result(result:result):
    return 1

@app.post("/population")
async def population():
    return {"population": init()}