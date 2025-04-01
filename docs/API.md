# API Documentation

Detailed documentation for the GenAI Banking Practice API endpoints.

## Authentication

### Register User
```http
POST /api/v1/auth/register
```

Request body:
```json
{
  "email": "user@example.com",
  "password": "strongpassword",
  "full_name": "John Doe"
}
```

Response:
```json
{
  "id": 1,
  "email": "user@example.com",
  "full_name": "John Doe",
  "is_active": true
}
```

### Login
```http
POST /api/v1/auth/login
```

Request body:
```json
{
  "username": "user@example.com",
  "password": "strongpassword"
}
```

Response:
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "bearer"
}
```

## Account Management

### Create Account
```http
POST /api/v1/accounts
```

Request body:
```json
{
  "account_type": "savings",
  "initial_deposit": 1000.00
}
```

Response:
```json
{
  "id": 1,
  "account_number": "1234567890",
  "account_type": "savings",
  "balance": 1000.00,
  "created_at": "2024-04-01T10:00:00Z"
}
```

### Get Account Details
```http
GET /api/v1/accounts/{account_id}
```

Response:
```json
{
  "id": 1,
  "account_number": "1234567890",
  "account_type": "savings",
  "balance": 1000.00,
  "created_at": "2024-04-01T10:00:00Z",
  "transactions": [
    {
      "id": 1,
      "amount": 1000.00,
      "transaction_type": "deposit",
      "description": "Initial deposit",
      "timestamp": "2024-04-01T10:00:00Z"
    }
  ]
}
```

## Transactions

### Create Transaction
```http
POST /api/v1/transactions
```

Request body:
```json
{
  "account_id": 1,
  "amount": 500.00,
  "transaction_type": "withdrawal",
  "description": "ATM withdrawal"
}
```

Response:
```json
{
  "id": 2,
  "account_id": 1,
  "amount": 500.00,
  "transaction_type": "withdrawal",
  "description": "ATM withdrawal",
  "timestamp": "2024-04-01T11:00:00Z"
}
```

### List Transactions
```http
GET /api/v1/transactions
```

Query parameters:
- `account_id`: Filter by account (optional)
- `start_date`: Filter by start date (optional)
- `end_date`: Filter by end date (optional)
- `transaction_type`: Filter by type (optional)

Response:
```json
{
  "items": [
    {
      "id": 1,
      "amount": 1000.00,
      "transaction_type": "deposit",
      "description": "Initial deposit",
      "timestamp": "2024-04-01T10:00:00Z"
    },
    {
      "id": 2,
      "amount": 500.00,
      "transaction_type": "withdrawal",
      "description": "ATM withdrawal",
      "timestamp": "2024-04-01T11:00:00Z"
    }
  ],
  "total": 2
}
```

## AI Features

### Analyze Transaction
```http
POST /api/v1/ai/analyze-transaction
```

Request body:
```json
{
  "transaction_id": 2
}
```

Response:
```json
{
  "analysis": {
    "fraud_score": 0.1,
    "category": "withdrawal",
    "risk_level": "low",
    "recommendations": [
      "Consider setting up transaction alerts",
      "Review recent similar transactions"
    ]
  }
}
```

### Chat with AI Assistant
```http
POST /api/v1/ai/chat
```

Request body:
```json
{
  "message": "What's my current balance?"
}
```

Response:
```json
{
  "response": "Your current balance in your savings account is $500.00. Would you like to see your recent transactions?"
}
```

## WebSocket Notifications

### Connect to WebSocket
```websocket
GET /ws/notifications
```

Connection requires authentication token in query parameter:
```
ws://localhost:8000/ws/notifications?token=your-jwt-token
```

### Message Format

Server-sent messages:
```json
{
  "type": "transaction",
  "data": {
    "account_id": 1,
    "amount": 500.00,
    "transaction_type": "deposit",
    "timestamp": "2024-04-01T12:00:00Z"
  }
}
```

## Error Responses

### 400 Bad Request
```json
{
  "detail": "Invalid request parameters"
}
```

### 401 Unauthorized
```json
{
  "detail": "Could not validate credentials"
}
```

### 404 Not Found
```json
{
  "detail": "Resource not found"
}
```

### 422 Validation Error
```json
{
  "detail": [
    {
      "loc": ["body", "amount"],
      "msg": "Amount must be greater than 0",
      "type": "value_error"
    }
  ]
}
```

## Rate Limiting

- API endpoints are rate-limited to 100 requests per minute per user
- WebSocket connections are limited to 1 connection per user
- AI endpoints are limited to 50 requests per hour per user 