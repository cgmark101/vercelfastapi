import os
from fastapi import FastAPI, Request, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from deta import Deta
from models import Payload
import json
import datetime

app = FastAPI()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

#KEY = os.getenv('DETA_PROJECT_KEY')

deta =Deta('b0dhigbe_TkBCtpTZ8cUfV6aJuHh3HmVjivH26bjh')
db = deta.Base('ot')



@app.get('/', include_in_schema=False)
async def index():
    return {'hola' : 'mundo'}

@app.post('/position/', include_in_schema=False)
async def post_position(request:Request):
    r = await request.body()
    r = r.decode('utf-8')
    r = json.loads(r)
    d = db.update(r, 'viiobn6mj1pf')
    return r

@app.post('/position2/')
async def post_position(payload:Payload):
    r = payload.dict()
    d = db.update(r, 'viiobn6mj1pf')
    return r

@app.post('/setup/')
async def post_position(payload:Payload):
    r = payload.dict()
    d = db.insert(r)
    return r

@app.get('/realtime/')
async def get_position():
    d = next(db.fetch())
    for items in d:
        lat = items['lat']
        lon = items['lon']
        geojson = {"geometry": {"type": "Point", "coordinates": [lon, lat]}, "type": "Feature", "properties": {}}
    return geojson

@app.get('/payload/')
async def get_payload():
    payload = db.get('viiobn6mj1pf')
    return payload
