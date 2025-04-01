from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base_class import Base
import enum

class TransactionType(str, enum.Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"
    TRANSFER = "transfer"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)
    is_active = Column(Boolean, default=True)
    
    accounts = relationship("Account", back_populates="owner")
    transactions = relationship("Transaction", back_populates="user")

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    account_number = Column(String, unique=True, index=True)
    balance = Column(Float, default=0.0)
    account_type = Column(String)  # savings, checking, etc.
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    owner = relationship("User", back_populates="accounts")
    transactions = relationship("Transaction", back_populates="account")

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    transaction_type = Column(Enum(TransactionType))
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    description = Column(String)
    account_id = Column(Integer, ForeignKey("accounts.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    
    account = relationship("Account", back_populates="transactions")
    user = relationship("User", back_populates="transactions") 