from pymongo import MongoClient

class MongoDb:

    def __init__(self):
        self.mongoUrl = 'localhost'
        self.client = MongoClient(self.mongoUrl)
        self.db = None
        self.dbName = ''
        self.collection = None
        self.collectionName = ''
        print('server_info',self.client.server_info())
        pass

    def selectDb(self, dbName):
        self.dbName = dbName
        self.db = self.client[self.dbName]
        print('list of collections:\n', self.db.list_collection_names())
        pass

    def selectColletion(self, collectionName):
        self.collectionName = collectionName
        self.collection = self.db[self.collectionName]
        pass

    def addDataToCalculate(self, jsonData, userId):
        data_id = self.collection.insert_one(jsonData).inserted_id
        print(f'{data_id}')
        return data_id

    def getData(self, searchMethod):
        print('finding in mongodb by: ', searchMethod)
        # return self.collection.find(searchMethod)
        rec = self.collection.find_one(searchMethod)
        # if rec == None:
        return rec

mdb = MongoDb()