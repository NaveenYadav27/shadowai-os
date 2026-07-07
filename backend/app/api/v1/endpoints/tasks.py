"""Tasks endpoints"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.dependencies import get_current_user
from pydantic import BaseModel
from typing import List

router = APIRouter()


class TaskCreate(BaseModel):
    workflow_id: str
    agent_id: str
    input_data: dict


class TaskResponse(BaseModel):
    id: str
    workflow_id: str
    agent_id: str
    status: str
    result: dict = None


@router.post("/", response_model=TaskResponse)
async def create_task(
    task: TaskCreate,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Create new task"""
    # TODO: Implement task creation
    return {
        "id": "1",
        "workflow_id": task.workflow_id,
        "agent_id": task.agent_id,
        "status": "pending",
    }


@router.get("/", response_model=List[TaskResponse])
async def list_tasks(
    workflow_id: str = None,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """List tasks"""
    # TODO: Implement task listing
    return []
