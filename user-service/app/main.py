from fastapi import FastAPI
from app.database import engine, Base
from app import models
from app.controllers import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="User Management Microservice",
    docs_url="/api/users/docs",
    openapi_url="/api/users/openapi.json"
)

app.include_router(router)
