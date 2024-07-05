# app/main.py

from fastapi import FastAPI, BackgroundTasks
from celery.result import AsyncResult
from app.celery_app import celery_app
from app.tasks import process_data

app = FastAPI()

@app.post("/submit-task/")
async def submit_task(data: str):
    task = process_data.delay(data)
    return {"task_id": task.id, "message": "Task submitted successfully"}

@app.get("/task-status/{task_id}")
async def get_task_status(task_id: str):
    task_result = AsyncResult(task_id, app=celery_app)
    if task_result.state == "PENDING":
        return {"task_id": task_id, "status": "Pending"}
    elif task_result.state == "SUCCESS":
        return {"task_id": task_id, "status": "Success", "result": task_result.result}
    elif task_result.state == "FAILURE":
        return {"task_id": task_id, "status": "Failure", "error": str(task_result.result)}
    else:
        return {"task_id": task_id, "status": task_result.state}
