from fastapi import FastAPI, Depends

import fastapi_db_sqlite
from api_web import place_api

app = FastAPI()
app.include_router(place_api.router)

fastapi_db_sqlite.setup_sqlalchemy()




@app.get('/')
async def root():
    return {'message': 'Hello World!'}
