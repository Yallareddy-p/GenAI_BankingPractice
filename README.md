# GenAI Banking Practice

A modern banking application that combines traditional banking operations with AI capabilities, built using FastAPI and LangChain.

## Features

- AI-powered customer support
- Intelligent transaction analysis
- Automated financial advice
- Natural language processing for banking queries
- Secure authentication and authorization
- Real-time notifications using Redis

## Tech Stack

- FastAPI
- LangChain
- OpenAI
- SQLAlchemy
- Redis
- Pydantic
- Python-Jose (JWT)
- Passlib (Password Hashing)

## Prerequisites

- Python 3.8+
- Redis server
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/GenAI_BankingPractice.git
cd GenAI_BankingPractice
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory with the following variables:
```
OPENAI_API_KEY=your_api_key
DATABASE_URL=your_database_url
REDIS_URL=your_redis_url
SECRET_KEY=your_secret_key
```

## Running the Application

1. Start the Redis server
2. Run the application:
```bash
uvicorn app.main:app --reload
```

The application will be available at `http://localhost:8000`

## API Documentation

Once the application is running, you can access:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Testing

Run the test suite:
```bash
pytest
```

## License

MIT License 