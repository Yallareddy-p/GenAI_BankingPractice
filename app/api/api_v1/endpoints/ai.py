from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.ai_service import AIService
from typing import Dict

router = APIRouter()
ai_service = AIService()

@router.post("/analyze-transaction")
async def analyze_transaction(
    transaction_id: int,
    db: Session = Depends(get_db)
) -> Dict:
    """
    Analyze a transaction using AI to detect potential fraud or provide insights
    """
    try:
        analysis = await ai_service.analyze_transaction(transaction_id, db)
        return {"status": "success", "analysis": analysis}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/chat")
async def chat_with_ai(
    message: str,
    db: Session = Depends(get_db)
) -> Dict:
    """
    Chat with the AI assistant about banking-related queries
    """
    try:
        response = await ai_service.chat(message, db)
        return {"status": "success", "response": response}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 