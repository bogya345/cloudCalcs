import pika
import sys
from client import rmqdb

params = pika.ConnectionParameters('127.0.0.1', 5672)
conn = pika.BlockingConnection(params)
channel = conn.channel()

channel.basic_publish(exchange='', routing_key='first', body='{"message":"bla", "total": 10}')

print('LOL')
