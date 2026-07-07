"""Health check endpoints"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter()


@router.get("/health", tags=["health"])
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "shadowai-os"}


@router.get("/health/db", tags=["health"])
async def database_health(db: Session = Depends(get_db)):
    """Database health check"""
    try:
        # Simple query to check database connection
        db.execute("SELECT 1")
        return {"status": "healthy", "component": "database"}
    except Exception as e:
        return {"status": "unhealthy", "component": "database", "error": str(e)}


@router.get("/ready", tags=["health"])
async def readiness_check():
    """Readiness check for Kubernetes"""
    return {"status": "ready"}
