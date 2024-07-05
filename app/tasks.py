# app/tasks.py

from app.celery_app import celery_app
import time
import socket

@celery_app.task()
def process_data(data):
    time.sleep(5)  # Simulate a time-consuming task
    # Get hostname of this computer
    hostname = socket.gethostname()
    # Calculate the character count
    char_count = len(data)
    return {"char_count": char_count, "worker": hostname}
