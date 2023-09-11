from fastapi.routing import APIRouter
from pydantic import Field
from auth.crud import check_is_admin_user, get_current_user
from fastapi import Depends,HTTPException,status
from auth.models import User
from auth.schemas import UserOut
from fastapi.responses import JSONResponse


from .models import Post
from .schemas import CreatePostSchema, PostOutSchema, ReactEnum, UpdatePostSchema

router=APIRouter()



@router.post('/',status_code=201,response_model=PostOutSchema, description='Admin Only')
async def create_post(payload:CreatePostSchema, isAdmin:bool|UserOut=Depends(check_is_admin_user)):
    if isAdmin==False:
        raise HTTPException(detail='You are unthorised to perform this action',status_code=status.HTTP_401_UNAUTHORIZED)
    try:
        post=await Post.create(title=payload.title, body=payload.body,user_id=isAdmin.id)
        return post
    except Exception as e:
        raise HTTPException(detail=str(e),status_code=status.HTTP_400_BAD_REQUEST)

   

@router.get('/', response_model=list[PostOutSchema],description='Publicly accessible')
async def get_posts():
    return await Post.filter(un_publish=False)

    
   
@router.get('/{post_id}', response_model=PostOutSchema,description='Publicly accessible')
async def get_post(post_id:int):
    try:
        return await PostOutSchema.from_queryset_single(Post.get(id=post_id))
    except Exception as e:
        raise HTTPException(detail=str(e), status_code=status.HTTP_404_NOT_FOUND)
 

@router.patch('/{post_id}/react',description='All authenticated users')
async def react(payload:ReactEnum,post_id:int,user:UserOut=Depends(get_current_user)):
    try:
        post=await Post.get(id=post_id)
        dislikes=[x['user'] for x in post.dislikes]
        likes=[x['user'] for x in post.likes]
        if payload.DISLIKE:
            if not user.username in dislikes and  not user.username in likes:
                post.dislikes.append({'user':user.username})
            else:
                post.dislikes.remove({'user':user.username})
        elif payload.LIKE:
            if not user.username in likes and not user.username in dislikes:
                post.likes.append({'user':user.username})
            else:
                post.likes.remove({'user':user.username})
        await post.save()
        return JSONResponse(content='Reaction saved successfully')
    except Exception as e :
        raise HTTPException(detail=str(e),status_code=status.HTTP_400_BAD_REQUEST)
        



@router.patch('/{post_id}',response_model=PostOutSchema,description='Adimin Only')
async def update_post(post_id:int, payload:UpdatePostSchema, admin:bool|UserOut=Depends(check_is_admin_user)):
    if admin==False:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='You are not authorised to perfom this action')
    else:
        try:
            post=await Post.get(id=post_id)
            if payload.title is not None:
                post.title=payload.title
            if payload.body is not None:
                post.body=payload.body
            if payload.un_publish is not None:
                post.un_publish=payload.un_publish
            await post.save()
            return post
        except Exception as e:
            raise HTTPException(detail=str(e),status_code=status.HTTP_400_BAD_REQUEST)



@router.delete('/{post_id}', description='Adimin Only')
async def delete_post(post_id:int, admin:UserOut|bool=Depends(check_is_admin_user)):
    if admin==False:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='You are not authorised to perfom this action')
    else:
        try:
            post=await Post.get(id=post_id)
            await post.delete()
            return JSONResponse(status_code=204, content='Post deleted')
        except Exception as e:
            raise HTTPException(detail=str(e), status_code=status.HTTP_404_NOT_FOUND)
        
