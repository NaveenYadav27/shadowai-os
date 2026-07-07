"""Workflows endpoints"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.dependencies import get_current_user
from pydantic import BaseModel
from typing import List

router = APIRouter()


class WorkflowCreate(BaseModel):
    name: str
    description: str = ""
    project_id: str


class WorkflowResponse(BaseModel):
    id: str
    name: str
    description: str
    project_id: str
    status: str = "draft"


@router.post("/", response_model=WorkflowResponse)
async def create_workflow(
    workflow: WorkflowCreate,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Create new workflow"""
    # TODO: Implement workflow creation
    return {
        "id": "1",
        "name": workflow.name,
        "description": workflow.description,
        "project_id": workflow.project_id,
        "status": "draft",
    }


@router.get("/", response_model=List[WorkflowResponse])
async def list_workflows(
    project_id: str = None,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """List workflows"""
    # TODO: Implement workflow listing
    return []
