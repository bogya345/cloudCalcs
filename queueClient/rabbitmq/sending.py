import queue
import pika
import sys

def __init__(host='127.0.0.1', port=5672):
    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters(host, port) # "/%2F"
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    pass

def createQueue(queueName):
    channel.queue_declare(queue=queueName)
    print(f'Queue ({queueName}) has been created')
    pass

def publish(queueName, message):
    channel.basic_publish(exchange='', routing_key=queueName, body=message)
    print(f'Msg({message}) has been published')
    pass

def closeConnetion():
    connection.close()
    print('RabbitMQ connetion has been closed')
    pass

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    pass


name = 'firstqueue'

# rmqdb.createQueue('firstqueue')
rmqdb.publish(name, 'lox')
rmqdb.closeConnetion()