# GenAI Banking Practice

A modern banking application that combines traditional banking operations with AI capabilities. Built using FastAPI, SQLAlchemy, and OpenAI integration.

## 🌟 Features

- 🏦 **Core Banking Operations**
  - User account management
  - Multiple account types (savings, checking)
  - Transaction processing
  - Balance tracking

- 🤖 **AI-Powered Features**
  - Transaction analysis
  - Fraud detection
  - Financial advice
  - AI chatbot for customer support

- 🔒 **Security**
  - JWT authentication
  - Password hashing
  - Role-based access control
  - Secure API endpoints

## 🏗️ Project Structure

```
GenAI_BankingPractice/
├── app/
│   ├── api/
│   │   └── api_v1/
│   │       ├── endpoints/
│   │       │   ├── ai.py         # AI-related endpoints
│   │       │   └── websocket.py  # WebSocket functionality
│   │       └── api.py            # API router configuration
│   ├── core/
│   │   └── config.py             # Application configuration
│   ├── db/
│   │   ├── base_class.py         # SQLAlchemy base class
│   │   ├── models.py             # Database models
│   │   └── session.py            # Database session management
│   ├── services/
│   │   ├── ai_service.py         # AI service implementation
│   │   └── notification_service.py# Real-time notifications
│   └── main.py                   # FastAPI application
├── tests/
│   └── test_ai_service.py        # AI service tests
├── .gitignore                    # Git ignore rules
├── requirements.txt              # Project dependencies
└── README.md                     # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Redis server
- OpenAI API key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Yallareddy-p/GenAI_BankingPractice.git
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

4. Create a .env file in the root directory:
```env
OPENAI_API_KEY=your_openai_api_key
DATABASE_URL=sqlite:///./banking.db
REDIS_URL=redis://localhost:6379
SECRET_KEY=your_secret_key
```

### Running the Application

1. Start the Redis server

2. Run the FastAPI application:
```bash
uvicorn app.main:app --reload
```

3. Access the application:
- API documentation: http://localhost:8000/docs
- ReDoc documentation: http://localhost:8000/redoc
- API root: http://localhost:8000/

## 📚 API Documentation

### Core Endpoints

#### Authentication
- `POST /api/v1/auth/login` - User login
- `POST /api/v1/auth/register` - User registration

#### Users
- `GET /api/v1/users/me` - Get current user
- `PUT /api/v1/users/me` - Update user details

#### Accounts
- `GET /api/v1/accounts` - List user accounts
- `POST /api/v1/accounts` - Create new account
- `GET /api/v1/accounts/{id}` - Get account details
- `PUT /api/v1/accounts/{id}` - Update account

#### Transactions
- `GET /api/v1/transactions` - List transactions
- `POST /api/v1/transactions` - Create transaction
- `GET /api/v1/transactions/{id}` - Get transaction details

### AI Features

#### Transaction Analysis
- `POST /api/v1/ai/analyze-transaction`
  ```json
  {
    "transaction_id": "123",
    "analysis": {
      "fraud_score": 0.1,
      "category": "shopping",
      "recommendations": ["..."]
    }
  }
  ```

#### AI Chat
- `POST /api/v1/ai/chat`
  ```json
  {
    "message": "What's my account balance?",
    "response": "Your current balance is..."
  }
  ```

## 🔐 Security

### Authentication
- JWT-based authentication
- Token expiration and refresh
- Password hashing using bcrypt

### Authorization
- Role-based access control
- Endpoint permission management
- API key validation for AI services

## 🗄️ Database Schema

### User Model
```python
class User(Base):
    id: Integer
    email: String
    hashed_password: String
    full_name: String
    is_active: Boolean
    is_superuser: Boolean
    accounts: Relationship[Account]
```

### Account Model
```python
class Account(Base):
    id: Integer
    account_number: String
    account_type: String
    balance: Float
    owner_id: Integer
    created_at: DateTime
    transactions: Relationship[Transaction]
```

### Transaction Model
```python
class Transaction(Base):
    id: Integer
    account_id: Integer
    amount: Float
    transaction_type: String
    description: String
    timestamp: DateTime
```

## 🧪 Testing

Run the test suite:
```bash
pytest
```

### Test Coverage
- Unit tests for AI services
- Integration tests for API endpoints
- Database model tests
- Authentication tests

## 🔄 Real-time Features

### WebSocket Notifications
- Real-time transaction updates
- Account balance changes
- Fraud alerts
- System notifications

## 🛠️ Development

### Adding New Features
1. Create new endpoints in `app/api/api_v1/endpoints/`
2. Add models in `app/db/models.py`
3. Implement services in `app/services/`
4. Add tests in `tests/`

### Code Style
- Follow PEP 8 guidelines
- Use type hints
- Document functions and classes
- Keep functions small and focused

## 📝 License

MIT License - feel free to use this project for learning and development.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request 