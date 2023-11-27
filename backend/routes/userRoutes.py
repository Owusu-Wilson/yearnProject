from fastapi import APIRouter

user_router = APIRouter()


@user_router.get('/user/login')
async def login():
    return {'message': "user login"}

@user_router.get('/user/create')
async def login():
    return {'message': "Create Use route"}
