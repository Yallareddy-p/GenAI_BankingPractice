from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "GenAI Banking Assistant"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Database
    DATABASE_URL: str
    
    # OpenAI
    OPENAI_API_KEY: str
    
    # Redis
    REDIS_URL: str
    
    # CORS
    BACKEND_CORS_ORIGINS: list[str] = ["*"]
    
    class Config:
        env_file = ".env"

settings = Settings() 