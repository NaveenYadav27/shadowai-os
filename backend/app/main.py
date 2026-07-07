"""ShadowAI OS - Main FastAPI Application"""
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse

from app.config import settings
from app.database import engine, Base
from app.api.v1 import api_router
from app.api.health import health_router
from app.middleware import LoggingMiddleware, ExceptionHandlerMiddleware

# Configure logging
logging.basicConfig(
    level=settings.LOG_LEVEL,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifecycle management"""
    # Startup
    logger.info("🚀 ShadowAI OS Starting up...")
    logger.info(f"Environment: {settings.ENVIRONMENT}")
    logger.info(f"Database: {settings.DATABASE_URL}")
    logger.info(f"Redis: {settings.REDIS_URL}")
    
    # Create tables
    Base.metadata.create_all(bind=engine)
    logger.info("✅ Database tables initialized")
    
    yield
    
    # Shutdown
    logger.info("🛑 ShadowAI OS Shutting down...")


# Create FastAPI application
app = FastAPI(
    title="ShadowAI OS",
    description="Enterprise AI Operating System for orchestrating AI agents",
    version="1.0.0",
    docs_url="/docs" if settings.API_DOCS_ENABLED else None,
    redoc_url="/redoc" if settings.REDOC_ENABLED else None,
    openapi_url="/openapi.json" if settings.API_DOCS_ENABLED else None,
    lifespan=lifespan,
)

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=settings.ALLOWED_HOSTS,
)

app.add_middleware(LoggingMiddleware)
app.add_middleware(ExceptionHandlerMiddleware)


# Routes
app.include_router(health_router, prefix="", tags=["health"])
app.include_router(api_router, prefix="/api/v1", tags=["api"])


# Root endpoint
@app.get("/", tags=["info"])
async def root():
    """Root endpoint"""
    return {
        "name": "ShadowAI OS",
        "version": "1.0.0",
        "docs": "/docs",
        "api": "/api/v1",
        "status": "operational",
    }


# Exception handlers
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Global exception handler"""
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"},
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        workers=settings.API_WORKERS,
        reload=settings.ENVIRONMENT == "development",
        log_level=settings.LOG_LEVEL.lower(),
    )
