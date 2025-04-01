from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.ai_service import BankingAIService
from app.models.transaction import Transaction
from typing import Dict, Any

router = APIRouter()
ai_service = BankingAIService()

@router.post("/analyze-transaction/{transaction_id}")
async def analyze_transaction(
    transaction_id: int,
    db: Session = Depends(get_db)
) -> Dict[str, Any]:
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    
    transaction_data = {
        "amount": transaction.amount,
        "type": transaction.transaction_type,
        "timestamp": transaction.timestamp,
        "description": transaction.description
    }
    
    return ai_service.analyze_transaction(transaction_data)

@router.post("/financial-advice/{user_id}")
async def get_financial_advice(
    user_id: int,
    db: Session = Depends(get_db)
) -> Dict[str, Any]:
    # Get user's recent transactions and account data
    transactions = db.query(Transaction).filter(Transaction.user_id == user_id).all()
    
    user_data = {
        "transactions": [
            {
                "amount": t.amount,
                "type": t.transaction_type,
                "timestamp": t.timestamp,
                "description": t.description
            }
            for t in transactions
        ]
    }
    
    return ai_service.get_financial_advice(user_data)

@router.post("/fraud-detection/{transaction_id}")
async def detect_fraud(
    transaction_id: int,
    db: Session = Depends(get_db)
) -> Dict[str, Any]:
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    
    transaction_data = {
        "amount": transaction.amount,
        "type": transaction.transaction_type,
        "timestamp": transaction.timestamp,
        "description": transaction.description
    }
    
    return ai_service.detect_fraud(transaction_data) 