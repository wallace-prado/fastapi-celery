# app/celery_app.py

from celery import Celery

celery_app = Celery(
    'tasks',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/0'
)

celery_app.conf.update(
    result_expires=3600,
)
