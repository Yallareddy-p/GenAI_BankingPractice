# Detailed Setup Guide

This guide provides step-by-step instructions for setting up the GenAI Banking Practice application.

## Development Environment Setup

### 1. Python Environment

1. Install Python 3.8 or higher:
   - Windows: Download from [python.org](https://www.python.org/downloads/)
   - Linux: `sudo apt-get install python3.8`
   - macOS: `brew install python@3.8`

2. Verify installation:
```bash
python --version
```

### 2. Virtual Environment

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/macOS:
```bash
source venv/bin/activate
```

### 3. Dependencies

Install project dependencies:
```bash
pip install -r requirements.txt
```

## Database Setup

### SQLite Database

1. The application uses SQLite by default. No additional setup required.
2. Database will be created automatically at first run.
3. Location: `./banking.db`

### Redis Setup

1. Install Redis:
- Windows: Use [Windows Subsystem for Linux](https://redis.io/docs/getting-started/installation/install-redis-on-windows/) or [Memurai](https://www.memurai.com/)
- Linux: `sudo apt-get install redis-server`
- macOS: `brew install redis`

2. Start Redis server:
- Windows (WSL): `sudo service redis-server start`
- Linux: `sudo systemctl start redis`
- macOS: `brew services start redis`

3. Verify Redis is running:
```bash
redis-cli ping
```
Should return: `PONG`

## Environment Variables

1. Create `.env` file in project root:
```env
# Database
DATABASE_URL=sqlite:///./banking.db

# Redis
REDIS_HOST=localhost
REDIS_PORT=6379

# Security
SECRET_KEY=your-secret-key-at-least-32-characters
ACCESS_TOKEN_EXPIRE_MINUTES=1440  # 24 hours

# OpenAI
OPENAI_API_KEY=your-openai-api-key
```

2. Get OpenAI API Key:
- Sign up at [OpenAI](https://platform.openai.com/)
- Create an API key
- Add to `.env` file

## Running the Application

### Development Server

1. Start the application:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

2. Access the application:
- API: http://localhost:8000
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Production Deployment

For production, use a proper ASGI server like Gunicorn:

```bash
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

## Testing

1. Run all tests:
```bash
pytest
```

2. Run specific test file:
```bash
pytest tests/test_ai_service.py
```

3. Run with coverage:
```bash
pytest --cov=app tests/
```

## Troubleshooting

### Common Issues

1. **Database Connection Error**
- Verify DATABASE_URL in .env
- Check file permissions
- Ensure directory is writable

2. **Redis Connection Error**
- Verify Redis is running
- Check REDIS_HOST and REDIS_PORT
- Try redis-cli ping

3. **OpenAI API Error**
- Verify API key is valid
- Check API key permissions
- Ensure sufficient API credits

### Getting Help

1. Check the [GitHub Issues](https://github.com/Yallareddy-p/GenAI_BankingPractice/issues)
2. Create a new issue with:
   - Error message
   - Steps to reproduce
   - Environment details 