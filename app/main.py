from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.api.api_v1.api import api_router
from app.core.config import settings
from app.db.session import engine
from app.db import models

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="GenAI Banking API",
    description="A modern banking API with AI capabilities",
    version="1.0.0"
)

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {
        "message": "Welcome to GenAI Banking API",
        "docs": "/docs",
        "redoc": "/redoc"
    } 