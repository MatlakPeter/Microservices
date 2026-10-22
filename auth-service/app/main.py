from fastapi import FastAPI
from app.database import engine, Base
from app import models
from app.controllers import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Authorization Microservice",
    docs_url="/api/auth/docs",
    openapi_url="/api/auth/openapi.json"
)

app.include_router(router)
