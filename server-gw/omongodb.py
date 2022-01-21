from pymongo import MongoClient

class MongoDb:

    def __init__(self):
        self.mongoUrl = 'localhost'
        self.client = MongoClient(self.mongoUrl)
        print(self.client.server_info())
        pass

    def addDataToCalculate(self, jsonData, userId):
        db = self.client['UserStorage']
        clt = db['Data']

        data_id = clt.insert_one(jsonData).inserted_id
        print(f'{data_id}')

        if(userId==None):
            userId = jsonData['user_id']

        return data_id

    def getData(self, searchMethod):
        self.client
        return 0

mdb = MongoDb()