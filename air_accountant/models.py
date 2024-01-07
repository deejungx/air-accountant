"""
Accounts Table:

Purpose: To list all accounts used in your business.
Fields:
Account Number (Text): Unique identifier for each account.
Account Name (Text): Name of the account (e.g., Cash, Accounts Receivable).
Type (Single Select): Categories like Asset, Liability, Equity, Revenue, Expense.
Description (Long text): Details about what the account is used for.


Transactions Table:

Purpose: To record all business transactions.
Fields:
Date (Date): The date of the transaction.
Description (Long text): Details of the transaction.
Amount (Currency): The monetary value of the transaction.
Account (Link to Accounts Table): Which account it affects.
Type (Single Select): Debit or Credit.


Journals Table:

Purpose: To group transactions into journals (e.g., Sales Journal, Purchase Journal).
Fields:
Journal Name (Text): Name of the journal.
Transactions (Link to Transactions Table): Entries that make up the journal.

"""
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
    date: date
    description: str
    amount: float = Field(gt=0)  # amount must be greater than 0
    account_id: int
    type: str  # Can be 'Debit' or 'Credit'


class Journal(BaseModel):
    journal_id: int
    journal_name: str
    transactions: List[Transaction]
