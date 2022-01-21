from aiohttp import web
import requests
import json

from oredis import rdb
from omongodb import mdb

routes = web.RouteTableDef()

# region POST handlers
@routes.post('/calculate', name='calculate')
async def receiveData(request):
    raw = await request.text()
    data = json.loads(raw)

    userId = data['user_id']
    # r = req.post('http://localhost:8080/calculate', data=raw)
    # r = req.post('http://localhost:8080/calculate', data=data['user_id'])

    dataId = mdb.addDataToCalculate(data, userId)
    
    key = f'{userId}'
    value = f'{dataId}'
    rdb.appendValue(key, value)

    return web.Response(text=f'Data has been stored successfully. Item ID is [{dataId}]')

# region GET handlers
@routes.get('/', name='hello')
def helloworld(request):
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

    return web.Response(text='Request in queue')

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

    res = requests.get(f'http://localhost:8080/correlation_sync?user_id={user_id}&x_data_type={x_data_type}&y_data_type={y_data_type}')
    print(res.json())

    return web.json_response(res.json())