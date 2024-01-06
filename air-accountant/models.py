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
