import json
from bson.objectid import ObjectId

# from redis import rdb
from mongodb import mdb

def getJsonObj(path='./test.json'):
    with open(path) as f:
        d = json.load(f)
        print(d)
        return d
def getJsonRaw(path='./test.json'):
    d = """
    {
    "user_id": 1,
    "x_data":[1,2,3,4,5,6],
    "y_data":[1,2,3,4,5,6]
    }
    """
    return d

# getJson()

def saveData():
    dataId = mdb.addDataToCalculate(getJsonObj(), 1)
    print(dataId)
    return dataId

def getData(dataId):
    data = mdb.getData({"_id":dataId})
    print(data)
    return data

mdb.selectDb('UserStorage')
mdb.selectColletion('Nums')

print('='*10+' saving data')
# dataId = saveData()
dataId = ObjectId('61e86c69ccafbf7b209ecebb')

print('='*10+' getting data')
getData(dataId)