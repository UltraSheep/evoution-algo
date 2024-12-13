import os
import datetime
from pathlib import Path
from .. import config

def initialize_environment():
    Path("./results").mkdir(exist_ok=True)
    with open(f"./results/{config.RESULTS_FILE}_{datetime.datetime.now().strftime('%Y_%m_%d_%H%M%S')}.txt", "w") as file:
        os.environ["result_file"]=file.name
        file.write(f"Population size = {config.POP_SIZE}\nTournament size = {config.TOURNAMENT_SIZE}\nEnemy per level = {config.ENEMY_COUNT}\n")
        file.close()