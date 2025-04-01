# Development Guide

This guide provides information for developers who want to contribute to or modify the GenAI Banking Practice application.

## Project Architecture

### Directory Structure
```
app/
├── api/              # API endpoints and routers
├── core/             # Core configuration and settings
├── db/               # Database models and session management
└── services/         # Business logic and services
```

### Component Overview

1. **API Layer** (`app/api/`)
   - REST endpoints
   - Request/response models
   - Input validation
   - Route handlers

2. **Core** (`app/core/`)
   - Configuration management
   - Environment variables
   - Constants
   - Base classes

3. **Database** (`app/db/`)
   - SQLAlchemy models
   - Database session
   - Migrations
   - Query utilities

4. **Services** (`app/services/`)
   - Business logic
   - External integrations
   - Data processing
   - AI functionality

## Development Workflow

### 1. Setting Up Development Environment

1. Clone the repository:
```bash
git clone https://github.com/Yallareddy-p/GenAI_BankingPractice.git
cd GenAI_BankingPractice
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 2. Code Style Guidelines

1. **Python Style**
   - Follow PEP 8
   - Use type hints
   - Maximum line length: 88 characters
   - Use docstrings for functions and classes

2. **Naming Conventions**
   - Classes: PascalCase
   - Functions/variables: snake_case
   - Constants: UPPER_CASE
   - Private methods/variables: _leading_underscore

3. **Code Organization**
   - One class per file
   - Related functions grouped in modules
   - Clear separation of concerns

### 3. Adding New Features

1. **Create a New Branch**
```bash
git checkout -b feature/your-feature-name
```

2. **Implement the Feature**
   - Add new endpoints in `app/api/`
   - Create models in `app/db/models.py`
   - Implement business logic in `app/services/`
   - Add tests in `tests/`

3. **Testing**
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_your_feature.py

# Run with coverage
pytest --cov=app tests/
```

4. **Code Review**
   - Write clear commit messages
   - Create detailed pull request
   - Address review comments

### 4. Database Changes

1. **Creating New Models**
```python
from app.db.base_class import Base
from sqlalchemy import Column, Integer, String

class YourModel(Base):
    __tablename__ = "your_table"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
```

2. **Database Migrations**
```bash
# Create migration
alembic revision --autogenerate -m "Add your_table"

# Apply migration
alembic upgrade head
```

### 5. Adding API Endpoints

1. **Create Route Handler**
```python
from fastapi import APIRouter, Depends
from app.db.session import get_db

router = APIRouter()

@router.post("/your-endpoint")
async def your_endpoint(
    data: YourSchema,
    db: Session = Depends(get_db)
):
    # Implementation
    pass
```

2. **Add to API Router**
```python
# In app/api/api_v1/api.py
from app.api.api_v1.endpoints import your_module

api_router.include_router(
    your_module.router,
    prefix="/your-prefix",
    tags=["your-tag"]
)
```

### 6. AI Integration

1. **Using OpenAI Service**
```python
from app.services.ai_service import AIService

ai_service = AIService()
response = await ai_service.analyze_data(your_data)
```

2. **Custom AI Models**
```python
class CustomAIService:
    def __init__(self):
        self.model = load_your_model()
    
    async def predict(self, data):
        return self.model.predict(data)
```

## Testing

### 1. Unit Tests

```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_your_endpoint():
    response = client.post(
        "/api/v1/your-endpoint",
        json={"key": "value"}
    )
    assert response.status_code == 200
    assert response.json()["result"] == "expected"
```

### 2. Integration Tests

```python
import pytest
from app.db.session import get_db

@pytest.mark.asyncio
async def test_database_integration():
    db = next(get_db())
    # Test database operations
    db.close()
```

### 3. Performance Testing

```python
import time

def test_endpoint_performance():
    start_time = time.time()
    response = client.get("/api/v1/your-endpoint")
    duration = time.time() - start_time
    assert duration < 0.5  # Should respond within 500ms
```

## Deployment

### 1. Production Configuration

1. Update `.env` file:
```env
ENVIRONMENT=production
LOG_LEVEL=INFO
WORKERS=4
```

2. Use production ASGI server:
```bash
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

### 2. Monitoring

1. Set up logging:
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

2. Health checks:
```python
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow()
    }
```

## Security

### 1. Authentication

```python
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    # Verify JWT token
    pass
```

### 2. Rate Limiting

```python
from fastapi import Request
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

@app.get("/rate-limited-endpoint")
@limiter.limit("5/minute")
async def rate_limited(request: Request):
    pass
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

Remember to:
- Write clear commit messages
- Add tests for new features
- Update documentation
- Follow code style guidelines 