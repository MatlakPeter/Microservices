from fastapi import FastAPI
from app.database import engine, Base
from app import models
from app.controllers import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Device Management Microservice",
    docs_url="/api/devices/docs",
    openapi_url="/api/devices/openapi.json"
)

app.include_router(router)
