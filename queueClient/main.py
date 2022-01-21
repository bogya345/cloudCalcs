from rabbitmq import receiving
import time
import json
import requests as req

def callback(ch, method, properties, body):
    print(f' [*]:Receiving: {body}')
    print(ch, method, properties, body)
    try:
        data = json.loads(body)
    except json.decoder.JSONDecodeError:
        print('Cant parse JSON message')

    print('message: ', data['message'])
    total = data['total']
    for i in range(0, total):
        time.sleep(1)
        print(f':{i}/{total} seconds:')

    req.get

    print('End of callback')
    pass

receiving.main(callback)