import os
import json
import datetime

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

from .structures import *

def visualize_data(manual_file: LOG = None):
    if manual_file:
        file_path = f"./results/manual_{datetime.datetime.now().strftime('%Y_%m_%d_%H%M%S')}"
        result_file = f'{file_path}/result.json'

        Path(file_path).mkdir(exist_ok=True)
        with open(result_file, "w") as file:
            file.write(manual_file.model_dump_json(indent=4))

        data = manual_file.model_dump()
    else:
        file_path = os.environ.get("result_path")
        result_file = f'{file_path}/result.json'

        with open(result_file, "r") as file:
            data = json.load(file)

    generations = []
    for generation in data["generations"]:
        for population in generation["pop"]:
            for enemy in population["enemies"]:
                generations.append({
                    "generation_id": generation["id"],
                    "score": population["score"],
                    "enemy_id": enemy["id"],
                    "health": enemy["health"],
                    "weapon": enemy["weapon"],
                    "speed": enemy["speed"],
                    "jump": enemy["jump"]
                })

    df = pd.DataFrame(generations)
    files = []
    
    # Visualization 1: Average Score per Generation
    image_name = f'{file_path}/average_score.png'
    avg_scores = df.groupby("generation_id")["score"].mean()
    plt.figure(figsize=(10, 6))
    plt.plot(avg_scores.index, avg_scores.values, marker="o", label="Average Score")
    plt.title("Average Score per Generation")
    plt.xlabel("Generation")
    plt.ylabel("Average Score")
    plt.grid(True)
    plt.legend()
    plt.savefig(image_name)
    files.append(image_name)

    # Visualization 2: Average Attributes per Generation
    image_name = f'{file_path}/average_attributes.png'
    avg_attributes = df.groupby("generation_id")[["health", "weapon", "speed", "jump"]].mean()
    avg_attributes.plot(figsize=(10, 6), marker="o")
    plt.title("Average Enemy Attributes per Generation")
    plt.xlabel("Generation")
    plt.ylabel("Attribute Value")
    plt.grid(True)
    plt.legend(title="Attributes")
    plt.savefig(image_name)
    files.append(image_name)

    # Visualization 3: Distribution of Scores within a Specific Generation
    image_name = f'{file_path}/distribution.png'
    specific_gen = 0
    gen_data = df[df["generation_id"] == specific_gen]
    plt.figure(figsize=(10, 6))
    plt.hist(gen_data["score"], bins=10, color="skyblue", edgecolor="black")
    plt.title(f"Score Distribution for Generation {specific_gen}")
    plt.xlabel("Score")
    plt.ylabel("Frequency")
    plt.grid(True)
    # plt.savefig(image_name)
    # files.append(image_name)

    return files