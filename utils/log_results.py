import os
import json
from .structures import *

def log(generation, population: POPULATION, result: RESULT):
    result_file = os.environ.get("result_file")

    generation_data = {
        "generation_id": generation,
        "groups": []
    }

    for i, level in enumerate(population.pop):
        group_data = {
            "group_id": i,
            "enemies": [],
            "score": result.fitness[i]
        }
        
        for enemy in level.enemies:
            enemy_data = {
                "id": enemy.id,
                "health": enemy.health,
                "weapon": enemy.weapon,
                "speed": enemy.speed,
                "jump": enemy.jump
            }
            group_data["enemies"].append(enemy_data)
        
        generation_data["groups"].append(group_data)

    with open(result_file, "r") as file:
        all_data = json.load(file)
    
    all_data["generations"].append(generation_data)
    
    with open(result_file, "w") as file:
        json.dump(all_data, file, indent=4)
