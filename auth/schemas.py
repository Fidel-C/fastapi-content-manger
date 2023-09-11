          
from pydantic import BaseModel
from tortoise.contrib.pydantic.creator import pydantic_model_creator

from auth.models import User



UserOut=pydantic_model_creator(User,exclude=('password','is_admin','is_active',),)

class RegisterSchema(BaseModel):
    username:str
    password:str
    
    
class Token(BaseModel):
    token_type:str
    access_token:str