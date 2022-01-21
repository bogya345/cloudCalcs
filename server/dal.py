from pymongo import MongoClient

class OwnClient:

    def __init__(self):
        self.mongoUrl = 'localhost'
        self.client = MongoClient(self.mongoUrl)
        pass

    def knock(self):
        print('knock-knock')
        pass

    def addDataToCalculate(self, jsonData, userId=None):
        db = self.client['UserStorage']
        clt = db['Data']

        data_id = clt.insert_one(jsonData).inserted_id
        print(f'{data_id}')

        if(userId==None):
            userId = 'lol'

        

        return

db = OwnClient()