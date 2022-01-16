from aiohttp import web
import requests as req
from pymongo import MongoClient
import json

routes = web.RouteTableDef()
mongoUrl = 'localhost'

# region POST handlers
@routes.post('/calculate', name='calculate')
def receiveData(request, data):
    print(request)

    client = MongoClient(mongoUrl), 

    pass

# region GET handlers
@routes.get('/', name='hello')
def helloworld(request):
    return web.Response(text='Hello World')

@routes.get('/correlation', name='correlation')
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
