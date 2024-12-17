import copy
import io

from PIL import Image
from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse

from .utils import *
from .config import train

current_population = None
generation = None
app = FastAPI()

class CustomORJSONResponse(Response):
    media_type = "application/json"

@app.get("/initialize")
async def initialize():
    initialize_environment()
    global current_population, generation
    generation = 0
    current_population = initialize_population()
    denormalized_population = copy.deepcopy(current_population)
    denormalized_population.denormalize()
    return {"population" : denormalized_population.pop}

@app.put("/next_generation")
async def next_generation(result: RESULT):
    global current_population , generation
    log (generation , current_population , result)
    generation += 1
    current_population = train(current_population , result)
    denormalized_population = copy.deepcopy(current_population)
    denormalized_population.denormalize()
    return {"population" : denormalized_population.pop}

@app.put("/result_visualization")
async def result_visualization(input_file: LOG = None):
    image_paths = visualize_data(input_file)
    images = [Image.open(image_path) for image_path in image_paths]

    total_width = max(img.width for img in images)
    total_height = sum(img.height for img in images)
    combined_image = Image.new("RGB", (total_width, total_height))

    y_offset = 0
    for img in images:
        combined_image.paste(img, (0, y_offset))
        y_offset += img.height

    buffer = io.BytesIO()
    combined_image.save(buffer, format="png")
    buffer.seek(0)

    return StreamingResponse(buffer, media_type="image/jpng")