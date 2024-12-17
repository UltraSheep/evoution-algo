import os
import json
import pandas as pd
import matplotlib.pyplot as plt

from .structures import *

def visualize_data(manual_file: LOG = None):
    if manual_file:
        data = manual_file.model_dump()
        result_file = "./results/manual"
    else:
        result_file = os.environ.get("result_file")
        if not result_file or not os.path.exists(result_file):
            raise FileNotFoundError("Result file not found. Make sure logging has been performed.")

        with open(result_file, "r") as file:
            data = json.load(file)
        result_file = result_file[:-5]

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
    image_path = f'{result_file}_fig1.png'
    avg_scores = df.groupby("generation_id")["score"].mean()
    plt.figure(figsize=(10, 6))
    plt.plot(avg_scores.index, avg_scores.values, marker="o", label="Average Score")
    plt.title("Average Score per Generation")
    plt.xlabel("Generation")
    plt.ylabel("Average Score")
    plt.grid(True)
    plt.legend()
    plt.savefig(image_path)
    files.append(image_path)

    # Visualization 2: Average Attributes per Generation
    image_path = f'{result_file}_fig2.png'
    avg_attributes = df.groupby("generation_id")[["health", "weapon", "speed", "jump"]].mean()
    avg_attributes.plot(figsize=(10, 6), marker="o")
    plt.title("Average Enemy Attributes per Generation")
    plt.xlabel("Generation")
    plt.ylabel("Attribute Value")
    plt.grid(True)
    plt.legend(title="Attributes")
    plt.savefig(image_path)
    files.append(image_path)

    # Visualization 3: Distribution of Scores within a Specific Generation
    image_path = f'{result_file}_fig2.png'
    specific_gen = 0
    gen_data = df[df["generation_id"] == specific_gen]
    plt.figure(figsize=(10, 6))
    plt.hist(gen_data["score"], bins=10, color="skyblue", edgecolor="black")
    plt.title(f"Score Distribution for Generation {specific_gen}")
    plt.xlabel("Score")
    plt.ylabel("Frequency")
    plt.grid(True)
    # plt.savefig(image_path)
    # files.append(image_path)

    return files