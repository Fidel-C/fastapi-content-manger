from httpx import AsyncClient
import pytest
from auth.crud import hash_pass
from auth.models import User
from fastapi import status


@pytest.mark.anyio
async def test_create_post(client: AsyncClient):
    data = {"title":"Post One", "body":"Post body of post one"}
    uname,passw=['admin3','admin456']
    newuser=await User.create(username=uname,password=hash_pass(passw),is_admin=True)
    token=newuser.create_token({'sub':newuser.username})
    response = await client.post("/posts/", json=data,headers={"Authorization":f"Bearer {token}"})
    assert response.status_code == status.HTTP_201_CREATED




@pytest.mark.anyio
async def test_get_posts(client: AsyncClient):
    response = await client.get("/posts/")
    assert response.status_code == 200