from tortoise import models,fields
from passlib.hash import bcrypt
from datetime import timedelta,datetime
import jwt

import settings

class User(models.Model):
    username=fields.CharField(max_length=20,unique=True)
    password=fields.TextField()
    is_admin=fields.BooleanField(default=False)
    is_active=fields.BooleanField(default=True)
    created_at=fields.DatetimeField(auto_now_add=True) 
    updated_at=fields.DatetimeField(auto_now=True)
    
    def verify_password(self,pwd):
        return bcrypt.verify(pwd,self.password)
        
        
    def create_token(self, data:dict,expiry:timedelta=None):
        to_encode=data.copy()        
        if expiry is None:
            exp=datetime.utcnow()+timedelta(minutes=30)
            to_encode.update({'exp':exp})
        else:
            exp=datetime.utcnow()+timedelta(minutes=expiry)
            to_encode.update({'exp':exp})
        token= jwt.encode(payload=to_encode,key=settings.SECRET)
        return token
    
    
    
        
  