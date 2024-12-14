import os

def log(generation, population, result):
    with open(os.environ['result_file'], "a") as file:
        file.write(f"Gen {generation} :\n")
        for i, level in enumerate(population.pop):
            file.write(f"    enemies:\n")
            for enemy in level.enemies:
                file.write(f"        {enemy}\n")
            file.write(f"    score: {result.fitness[i]}\n\n")