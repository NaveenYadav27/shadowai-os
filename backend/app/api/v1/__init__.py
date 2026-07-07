"""API v1 routes"""
from fastapi import APIRouter
from app.api.v1.endpoints import (
    projects,
    workflows,
    tasks,
    agents,
    artifacts,
    auth,
)

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
api_router.include_router(workflows.router, prefix="/workflows", tags=["workflows"])
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
api_router.include_router(agents.router, prefix="/agents", tags=["agents"])
api_router.include_router(artifacts.router, prefix="/artifacts", tags=["artifacts"])
