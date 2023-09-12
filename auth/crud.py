from fastapi import Depends, HTTPException,status
from fastapi.responses import UJSONResponse,JSONResponse
from fastapi.routing import APIRouter
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from jwt import PyJWKError
import jwt
from auth.models import User

from auth.schemas import RegisterSchema, UserOut,Token
from passlib.hash import bcrypt
import settings
from datetime import datetime


router=APIRouter()






auth_scheme=OAuth2PasswordBearer(tokenUrl='auth/login')


        

@router.post('/register',status_code=status.HTTP_201_CREATED,response_model=UserOut)
async def register(form:RegisterSchema):
    exist=await User.exists(username=form.username)
    if exist:
        raise HTTPException(detail='User Exists',status_code=status.HTTP_403_FORBIDDEN)
    else:
        hash=hash_pass(form.password)
        user=await User.create(username=form.username,password=hash)       
        return user
        
        

def hash_pass(pawd:str):
    return bcrypt.hash(pawd)
    



@router.post('/login',response_model=Token)
async def login(form:OAuth2PasswordRequestForm=Depends()):
    #get user frm the database or throw 404
    exists=await User.get_or_none(username=form.username)
    if exists is None:
        raise HTTPException(detail='Incorrect login details',status_code=status.HTTP_404_NOT_FOUND)
    else:
        is_user=exists.verify_password(form.password)
        if is_user is False:
            raise HTTPException(detail='Incorrect login details',status_code=status.HTTP_404_NOT_FOUND)
        else:    
            token=exists.create_token({'sub':exists.username},expiry=settings.EXPIRY)
            return Token(token_type='bearer',access_token=token)



async def get_current_user(token:str=Depends(auth_scheme)):
    try:
        username=jwt.decode(token,settings.SECRET,algorithms='HS256').get('sub') 
    except (jwt.ExpiredSignatureError,jwt.InvalidTokenError,) as e:
        raise HTTPException(detail='Invalid/Expired Token',status_code=status.HTTP_401_UNAUTHORIZED)
    exists=await User.get_or_none(username=username)
    if exists is None:
        return False
    return await UserOut.from_tortoise_orm(exists)



async def check_is_admin_user(user:UserOut=Depends(get_current_user)):
    found=await User.get(id=user.id)
    if found.is_admin==True:
        return found
    else:
        return False
  
        
    
        
                
        
@router.get('/me',response_model=UserOut)
async def get_active_user(user:UserOut|bool=Depends(get_current_user)):
    if user is False:
        raise HTTPException(detail='Unauthenticated',status_code=status.HTTP_403_FORBIDDEN)
    else:
        return user

        

 
@router.get('/users',response_model=list[UserOut])
async def get_users(isAdmin:bool|UserOut=Depends(check_is_admin_user)):
    if isAdmin==False:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='You are not authorised to perform this action')
    return await User.all()
    
    
        
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        
        
