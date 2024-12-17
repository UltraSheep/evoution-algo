import os

from .structures import *

def log(generation, population: POPULATION, result: RESULT):
    result_file = os.environ.get("result_file")

    with open(result_file, "r") as file:
        data = LOG.model_validate_json(file.read())

    generation_data = POPULATION(
        id=generation,
        pop=[
            LEVEL(
                enemies=[
                    INDIVIDUAL(
                        id=enemy.id,
                        health=enemy.health,
                        weapon=enemy.weapon,
                        speed=enemy.speed,
                        jump=enemy.jump
                    ) for enemy in level.enemies
                ],
                score=result.fitness[i]
            ) for i, level in enumerate(population.pop)
        ]
    )

    data.generations.append(generation_data)

    with open(result_file, "w") as file:
        file.write(data.model_dump_json(indent=4))
