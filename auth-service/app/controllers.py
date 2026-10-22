from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter(prefix="/api/auth", tags=["Authentication"])

@router.get("/health")
def health_check(db: Session = Depends(get_db)):
    return {"service": "auth-service", "status": "up"}
