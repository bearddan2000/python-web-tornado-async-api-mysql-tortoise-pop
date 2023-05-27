from fastapi import FastAPI
import uvicorn
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator

import settings
from model import Pop
    
app = FastAPI()

register_tortoise(
    app,
    db_url= '{engine}://{username}:{password}@{host}/{db_name}'.format(
    **settings.MYSQL),
    modules={'models': ['model']}
)

@app.get('/pop')
async def get_all_pop():
    pops = pydantic_model_creator(Pop)
    return await pops.from_queryset(Pop.all())
    
if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0')
