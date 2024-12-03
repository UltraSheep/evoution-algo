from fastapi import FastAPI
from ..compare_algorithms import run_test
import pkgutil

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