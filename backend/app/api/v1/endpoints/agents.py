"""Agents endpoints"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.dependencies import get_current_user
from pydantic import BaseModel
from typing import List

router = APIRouter()


class AgentResponse(BaseModel):
    id: str
    name: str
    role: str
    capability: str
    status: str = "available"


@router.get("/", response_model=List[AgentResponse])
async def list_agents(
    capability: str = None,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """List available agents"""
    # TODO: Implement agent listing
    return []


@router.get("/{agent_id}", response_model=AgentResponse)
async def get_agent(
    agent_id: str,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get agent by ID"""
    # TODO: Implement agent retrieval
    return {
        "id": agent_id,
        "name": "Sample Agent",
        "role": "Developer",
        "capability": "Backend Development",
        "status": "available",
    }
