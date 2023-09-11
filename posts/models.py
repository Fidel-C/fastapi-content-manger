from tortoise import fields,models

# from ..auth.models import User
from auth.models import User



class Post(models.Model):
    title=fields.CharField(max_length=200,unique=True)
    body=fields.TextField()
    user:fields.ForeignKeyRelation['User'] = fields.ForeignKeyField('models.User',related_name='posts',on_delete=fields.CASCADE, null=True)
    dislikes=fields.JSONField(null=True,default=[])
    likes=fields.JSONField(null=True,default=[])
    un_publish=fields.BooleanField(default=False)
    created_at=fields.DatetimeField(auto_now_add=True)
    updated_at=fields.DatetimeField(auto_now=True)
    
    
    