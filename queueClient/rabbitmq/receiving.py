import pika, sys, os

def main(callback, queueName='first'):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1', port=5672))
    channel = connection.channel()

    channel.queue_declare(queue=queueName)

    # def callback(ch, method, properties, body):
    #     print(" [x] Received %r" % body)
    #     pass

    channel.basic_consume(queue=queueName, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    pass

# if __name__ == '__main__':
#     try:
#         main()
#     except KeyboardInterrupt:
#         print('Interrupted')
#         try:
#             sys.exit(0)
#         except SystemExit:
#             os._exit(0)
#     pass