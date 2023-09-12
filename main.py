import asyncio
from tortoise.contrib.fastapi import register_tortoise
from auth.models import User

from fastapi import FastAPI,Request,testclient,status
from tortoise import Tortoise, run_async
from posts.crud import router as posts_router
from auth.crud import router as auth_router
from auth.crud import hash_pass
import sys,pytest
from fastapi.middleware.cors import CORSMiddleware
import settings   
from utils.rate_limiter import rate_limit


      



app=FastAPI(description='Content Management App',title='Content API', version='1.0')




  

register_tortoise(
    app=app,
    db_url='sqlite://database.sqlite',
    modules={'models':('auth.models','posts.models',)},
    generate_schemas=True,
    
)
Tortoise.init_models(['auth.models','posts.models'],'models')



#implementation of rate limiting

@app.get('/', description='Index')
@rate_limit(max_calls=10,time_frame=60)
async def index(req:Request):
    
    return {'content':'app'}

    
    
    
    
         
 
app.include_router(auth_router,prefix='/auth',tags=['Auth'])
app.include_router(posts_router,prefix='/posts',tags=['Posts'])






def receive_signal(signalNumber, frame):
    print('Received:', signalNumber)
    sys.exit()




# @app.on_event('startup')
# async def initialise_db():
#     # init_db(app)
#     await User.bulk_create([User(username='admin', password=hash_pass('admin123'),is_admin=True),User(username='johndoe',password=hash_pass('test123'))])
     
     
origins = settings.ALLOWED_ORIGINS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


       
