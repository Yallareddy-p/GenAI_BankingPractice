from fastapi import APIRouter
from app.api.api_v1.endpoints import users, accounts, transactions, ai

api_router = APIRouter()

api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(accounts.router, prefix="/accounts", tags=["accounts"])
api_router.include_router(transactions.router, prefix="/transactions", tags=["transactions"])
api_router.include_router(ai.router, prefix="/ai", tags=["ai"]) 