from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter(prefix="/api/devices", tags=["Devices"])

@router.get("/health")
def health_check(db: Session = Depends(get_db)):
    return {"service": "device-service", "status": "up"}
