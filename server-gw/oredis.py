import redis

class Redis:
    def __init__(self, host='127.0.0.1', port=8082, db=0,
     password=None, socket_timeout=None, decode_responses=True) -> None:
        self.db = redis.Redis(host=host, port=port, db=db,
        password=password, socket_timeout=socket_timeout, decode_responses=decode_responses)
        print(self.db.ping())
        pass

    def appendValue(self, key, value):
        item = {key: value}
        print('Redis: Item has been saved:\n', item)
        self.db.set(key, value)
        pass

    def getValue(self, key):
        item = self.db.get(key)
        print('Redis: Item has been received:\n', item)
        return item

rdb = Redis(host='127.0.0.1', port=8082)