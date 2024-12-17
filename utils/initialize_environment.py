import os
import datetime

from pathlib import Path

from .. import config
from .structures import *

def initialize_environment():
    Path("./results").mkdir(exist_ok=True)
    
    file_name = f"./results/{config.RESULTS_FILE}_{datetime.datetime.now().strftime('%Y_%m_%d_%H%M%S')}.json"
    
    initial_data = LOG(
        population_size=config.POP_SIZE,
        tournament_size=config.TOURNAMENT_SIZE,
        enemies_per_level=config.ENEMY_COUNT,
        generations=[]
    )
    
    with open(file_name, "w") as file:
        os.environ["result_file"] = file_name
        file.write(initial_data.model_dump_json(indent=4))
