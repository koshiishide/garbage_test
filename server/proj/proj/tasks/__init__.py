# celery_handson/celery_handson/tasks/__init__.py
from ..celery import app
import time

@app.task()
def add_numbers(a, b):
    print('Request: {}'.format(a + b))
    time.sleep(10)


    return a + b +3
