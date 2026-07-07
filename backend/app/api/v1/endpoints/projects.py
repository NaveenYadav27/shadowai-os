"""Projects endpoints"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.dependencies import get_current_user
from pydantic import BaseModel
from typing import List

router = APIRouter()


class ProjectCreate(BaseModel):
    name: str
    description: str = ""


class ProjectResponse(BaseModel):
    id: str
    name: str
    description: str


@router.post("/", response_model=ProjectResponse)
async def create_project(
    project: ProjectCreate,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Create new project"""
    # TODO: Implement project creation
    return {"id": "1", "name": project.name, "description": project.description}


@router.get("/", response_model=List[ProjectResponse])
async def list_projects(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """List projects"""
    # TODO: Implement project listing
    return []


@router.get("/{project_id}", response_model=ProjectResponse)
async def get_project(
    project_id: str,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get project by ID"""
    # TODO: Implement project retrieval
    return {"id": project_id, "name": "Sample Project", "description": ""}
