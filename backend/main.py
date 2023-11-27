from fastapi import FastAPI
from routes.adminRoutes import admin_router
from routes.userRoutes import user_router

app = FastAPI()

app.include_router(admin_router)
app.include_router(user_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
app.include_router(admin_router)
app.include_router(user_router)