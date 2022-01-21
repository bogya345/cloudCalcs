import queue
import pika
import sys

class RabbitMQ:

    def __init__(self, host='127.0.0.1', port=5672):
        self.credentials = pika.PlainCredentials('guest', 'guest')
        self.parameters = pika.ConnectionParameters(host, port) # "/%2F"
        self.connection = pika.BlockingConnection(self.parameters)
        self.channel = self.connection.channel()
        pass

    def createQueue(self, queueName):
        self.channel.queue_declare(queue=queueName)
        print(f'Queue ({queueName}) has been created')
        pass

    def publish(self, queueName, message):
        self.channel.basic_publish(exchange='', routing_key=queueName, body=message)
        print(f'Msg({message}) has been published')
        pass

    def closeConnetion(self):
        self.connection.close()
        print('RabbitMQ connetion has been closed')
        pass

    def callback(self, ch, method, properties, body):
        print(" [x] Received %r" % body)
        pass


rmqdb = RabbitMQ()
# name = 'firstqueue'

# # rmqdb.createQueue('firstqueue')
# rmqdb.publish(name, 'lox')
# rmqdb.closeConnetion()