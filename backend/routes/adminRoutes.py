from fastapi import APIRouter

admin_router = APIRouter()


@admin_router.get('/admin/login')
async def login():
    return {'message': 'Admin login'}
@admin_router.get('/admin/create')
async def login():
    return {'message': 'Create admin '}
