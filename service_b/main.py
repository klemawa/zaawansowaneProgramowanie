from fastapi import FastAPI
from pydantic import BaseModel
import pika
import os
import json

app = FastAPI()
RABBIT_HOST = os.environ.get('RABBITMQ_HOST', 'localhost')

class ImageRequest(BaseModel):
    url: str

@app.post("/analyze")
def analyze_image(request: ImageRequest):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBIT_HOST))
    channel = connection.channel()
    channel.queue_declare(queue='image_tasks', durable=True)

    #zadanie do kolejki
    channel.basic_publish(
        exchange='',
        routing_key='image_tasks',
        body=json.dumps({'url': request.url}),
        properties=pika.BasicProperties(delivery_mode=2)
    )
    connection.close()
    return {"message": "Przyjęto do kolejki", "filename": request.url}