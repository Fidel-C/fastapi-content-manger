from tortoise.contrib.pydantic.creator import pydantic_model_creator
from pydantic import BaseModel

from posts.models import Post
import enum
from typing import Optional
from pydantic import Field

class CreatePostSchema(BaseModel):
    title:str
    body:str

class ReactEnum(enum.Enum):
    LIKE='like'
    DISLIKE='dislike'
    
    
PostOutSchema=pydantic_model_creator(Post)    



class UpdatePostSchema(BaseModel):
    title:str or None=None
    body:str or None=None
    un_publish:bool or None=None
       