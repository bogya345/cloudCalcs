from aiohttp import web
import requests as req
import json
from bson.objectid import ObjectId
import ownMath

from oredis import rdb
from omongodb import mdb

routes = web.RouteTableDef()

# region POST handlers
# @routes.post('/calculate', name='calculate')
# async def receiveData(request):
#     raw = await request.text()
#     print('Received raw data:', raw)
#     data = json.loads(raw)
#     print('Parsed raw data:', data)

#     # db.

#     return web.Response(text='Data has been stored successfully')

# region GET handlers
@routes.get('/', name='hello')
def helloworld(request):
    rdb.knock()
    return web.Response(text='Hello World')

@routes.get('/correlation_async', name='correlation_async')
def calculateCorrelation(request):
    queryUrl = request.rel_url.query
    
    try:
        user_id = queryUrl['user_id']
        x_data_type = queryUrl['x_data_type']
        y_data_type = queryUrl['y_data_type']
    except:
        return web.Response(text='Something wrong with parametets.')

    print(user_id, x_data_type, y_data_type)

    return web.Response(text='Nothing to calculate yet')

@routes.get('/correlation_sync', name='correlation_sync')
def calculateCorrelation(request):
    queryUrl = request.rel_url.query
    
    try:
        user_id = queryUrl['user_id']
        x_data_type = queryUrl['x_data_type']
        y_data_type = queryUrl['y_data_type']
    except:
        return web.Response(text='Something wrong with parametets.')

    print(user_id, x_data_type, y_data_type)

    dataId = rdb.getValue(user_id)
    print(f'Got dataId({dataId}) from userId({user_id})')
    
    mdb.selectDb('UserStorage')
    mdb.selectColletion('Data')
    data = mdb.getData({"_id":ObjectId(dataId)})
    print('Got data:\n',data)

    pval_own = ownMath.pearsonCorrelationCoeff(data['x_data'], data['y_data'])
    pval_scipy = ownMath.pearsonCorrelationCoeff_scipy(data['x_data'], data['y_data'])

    response = {
        'pval_own': pval_own,
        'pval_scipy': pval_scipy
    }
    print('Prepared response:', response)

    return web.json_response(json.dumps(response))
