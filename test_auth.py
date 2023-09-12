import pytest
from httpx import AsyncClient
from auth.crud import hash_pass

from auth.models import User


@pytest.mark.anyio
async def test_register(client: AsyncClient):
    uname, passw = ["admin2", "admin123"]
    assert await User.filter(username=uname).count() == 0

    data = {"username": uname, "password":hash_pass(passw)}
    response = await client.post("/auth/register", json=data)
    # assert response.json() == dict(data, id=1)
    assert response.status_code == 201
    
@pytest.mark.anyio   
async def test_get_active_user(client:AsyncClient):
    uname, passw = ["admin", "admin123"]
    newUser=await User.create(username=uname,password=hash_pass(passw))
    token=newUser.create_token({'sub':newUser.username})
    data = {"username": uname, "password":passw}
    response = await client.get("/auth/me", headers={'Authorization':f'Bearer {token}'})
    assert response.status_code==200
 
    

    # response = await client.get("/auth/users")
    # assert response.status_code == 200
    # # assert response.json() == [dict(data, id=1)]

    # assert await User.filter(username=uname).count() == 1