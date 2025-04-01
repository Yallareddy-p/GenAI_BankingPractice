import pytest
from app.services.ai_service import BankingAIService
from app.models.transaction import TransactionType

@pytest.fixture
def ai_service():
    return BankingAIService()

def test_analyze_transaction(ai_service):
    transaction_data = {
        "amount": 1000.0,
        "type": TransactionType.DEPOSIT,
        "timestamp": "2024-01-01T10:00:00",
        "description": "Salary deposit"
    }
    
    result = ai_service.analyze_transaction(transaction_data)
    assert isinstance(result, dict)
    assert "risk_assessment" in result
    assert "spending_category" in result
    assert "suspicious_patterns" in result
    assert "recommendations" in result

def test_get_financial_advice(ai_service):
    user_data = {
        "transactions": [
            {
                "amount": 1000.0,
                "type": TransactionType.DEPOSIT,
                "timestamp": "2024-01-01T10:00:00",
                "description": "Salary deposit"
            },
            {
                "amount": -500.0,
                "type": TransactionType.WITHDRAWAL,
                "timestamp": "2024-01-02T15:00:00",
                "description": "Grocery shopping"
            }
        ]
    }
    
    result = ai_service.get_financial_advice(user_data)
    assert isinstance(result, dict)
    assert "spending_analysis" in result
    assert "budget_recommendations" in result
    assert "investment_suggestions" in result
    assert "risk_assessment" in result

def test_detect_fraud(ai_service):
    transaction_data = {
        "amount": 10000.0,
        "type": TransactionType.WITHDRAWAL,
        "timestamp": "2024-01-01T03:00:00",
        "description": "ATM withdrawal"
    }
    
    result = ai_service.detect_fraud(transaction_data)
    assert isinstance(result, dict)
    assert "fraud_risk_score" in result
    assert "suspicious_indicators" in result
    assert "recommended_actions" in result
    assert "confidence_level" in result 