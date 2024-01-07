from pydantic import BaseModel, Field
from datetime import date
from typing import List, Optional
from enum import Enum


class AccountTypeEnum(str, Enum):
    asset = "Asset"
    liability = "Liability"
    equity = "Equity"
    revenue = "Revenue"
    expense = "Expense"


class Account(BaseModel):
    account_number: int  # auto-increment setup on airtable
    account_name: str
    type: AccountTypeEnum  # Can be 'Asset', 'Liability', 'Equity', 'Revenue', or 'Expense'
    description: Optional[str] = None


class Transaction(BaseModel):
    transaction_id: int
    date: Optional[date]
    description: str
    amount: float = Field(gt=0)  # amount must be greater than 0
    account_id: int
    type: str  # Can be 'Debit' or 'Credit'


class Journal(BaseModel):
    journal_id: int
    date: date
    journal_name: str
    transactions: List[Transaction]
