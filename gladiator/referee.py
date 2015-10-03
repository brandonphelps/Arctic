

from celery import Celery
import time
import random

app = Celery('referee', broker='amqp://celery_user:helloworldilikecheese@10.20.1.2/celery_vhost', backend='amqp')

@app.task(name="gladiator.referee.run_game")
def run_game(client1, client2):
    time.sleep(random.random() * random.randint(1,10))
    return random.choice([client1, client2])
