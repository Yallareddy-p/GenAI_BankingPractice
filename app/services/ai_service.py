from openai import AsyncOpenAI
from app.core.config import settings
from sqlalchemy.orm import Session
from typing import Dict, Any

class AIService:
    def __init__(self):
        self.client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)

    async def analyze_transaction(self, transaction_id: int, db: Session) -> Dict[str, Any]:
        """
        Analyze a transaction using AI to detect potential fraud or provide insights
        """
        # Get transaction from database
        transaction = db.query("Transaction").filter_by(id=transaction_id).first()
        if not transaction:
            raise ValueError("Transaction not found")

        # Prepare prompt for AI
        prompt = f"""
        Please analyze this banking transaction:
        Amount: ${transaction.amount}
        Type: {transaction.transaction_type}
        Description: {transaction.description}
        Time: {transaction.timestamp}
        
        Provide insights about:
        1. Potential fraud indicators
        2. Spending category
        3. Financial advice
        """

        response = await self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a banking AI assistant specializing in transaction analysis and fraud detection."},
                {"role": "user", "content": prompt}
            ]
        )
        
        return {
            "analysis": response.choices[0].message.content,
            "transaction_id": transaction_id
        }

    async def chat(self, message: str, db: Session) -> Dict[str, Any]:
        """
        Chat with the AI assistant about banking-related queries
        """
        response = await self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful banking assistant. Provide clear, accurate information about banking services, financial advice, and account management."},
                {"role": "user", "content": message}
            ]
        )
        
        return {
            "message": message,
            "response": response.choices[0].message.content
        } 