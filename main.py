from contextlib import contextmanager
from nicegui import ui
from compare_algorithms import start
import asyncio
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor()

@contextmanager
def disable(button: ui.button):
    button.disable()
    try:
        yield
    finally:
        button.enable()

async def test(button):
    with disable(button):
        with ui.row():  # Explicit container to hold the notification
            ui.notify('Started')  # Notify the user
        # Run the blocking start() function in a thread
        result = await asyncio.get_event_loop().run_in_executor(executor, start)
        with ui.row():  # Another container for the result
            ui.label(result)  # Update the UI with the result

# Define the button and pass itself as a parameter to the `on_click` function
start_button = ui.button('Start', on_click=lambda: asyncio.create_task(test(start_button)))

ui.run(title='My App')
