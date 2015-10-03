from celery import Celery

app = Celery('test', broker='amqp://arena_celery:missingnotedstoppedpractice@r99acm.device.mst.edu/arena_vhost', backend='amqp')

@app.task
def add(x, y):
    return x + y

@app.task
def sub(x, y):
    return x - y
