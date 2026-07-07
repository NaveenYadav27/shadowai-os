"""Authentication endpoints"""
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth.jwt_handler import create_access_token
from pydantic import BaseModel

router = APIRouter()


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


@router.post("/login", response_model=TokenResponse)
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    """Login endpoint"""
    # TODO: Implement user authentication
    token = create_access_token({"sub": request.username})
    return {"access_token": token, "token_type": "bearer"}


@router.post("/register")
async def register(request: LoginRequest, db: Session = Depends(get_db)):
    """Register endpoint"""
    # TODO: Implement user registration
    return {"message": "User registered successfully"}
