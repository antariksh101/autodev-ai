from fastapi import FastAPI
from app.api.build_routes import router

app = FastAPI()

app.include_router(router)