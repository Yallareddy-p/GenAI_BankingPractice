from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from app.core.config import settings
from typing import List, Dict, Any
import json

class BankingAIService:
    def __init__(self):
        self.llm = OpenAI(
            api_key=settings.OPENAI_API_KEY,
            temperature=0.7
        )
        
    def analyze_transaction(self, transaction_data: Dict[str, Any]) -> Dict[str, Any]:
        prompt = PromptTemplate(
            input_variables=["transaction"],
            template="""
            Analyze the following banking transaction and provide insights:
            Transaction: {transaction}
            
            Please provide:
            1. Risk assessment (low/medium/high)
            2. Spending category
            3. Any suspicious patterns
            4. Recommendations
            
            Format the response as JSON.
            """
        )
        
        chain = LLMChain(llm=self.llm, prompt=prompt)
        result = chain.run(transaction=json.dumps(transaction_data))
        return json.loads(result)
    
    def get_financial_advice(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        prompt = PromptTemplate(
            input_variables=["user_data"],
            template="""
            Based on the following user's financial data, provide personalized advice:
            User Data: {user_data}
            
            Please provide:
            1. Spending analysis
            2. Budget recommendations
            3. Investment suggestions
            4. Risk assessment
            
            Format the response as JSON.
            """
        )
        
        chain = LLMChain(llm=self.llm, prompt=prompt)
        result = chain.run(user_data=json.dumps(user_data))
        return json.loads(result)
    
    def detect_fraud(self, transaction_data: Dict[str, Any]) -> Dict[str, Any]:
        prompt = PromptTemplate(
            input_variables=["transaction"],
            template="""
            Analyze the following transaction for potential fraud:
            Transaction: {transaction}
            
            Please provide:
            1. Fraud risk score (0-100)
            2. Suspicious indicators
            3. Recommended actions
            4. Confidence level
            
            Format the response as JSON.
            """
        )
        
        chain = LLMChain(llm=self.llm, prompt=prompt)
        result = chain.run(transaction=json.dumps(transaction_data))
        return json.loads(result) 