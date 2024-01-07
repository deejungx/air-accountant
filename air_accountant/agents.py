"""
Step 1: Analyze the Transaction
- Understand the Transaction: Determine what the transaction was for and the type.
- Identify Accounts Affected: Identify which accounts are impacted by the transaction.
Typically, there are at least two accounts involved.

Step 2: Determine the Type of Entry
- Debit and Credit: Based on double-entry accounting, decide which account should be debited
(increased if an asset or expense, decreased if liability or equity) and which should be credited
(decreased if an asset or expense, increased if liability or equity).

Step 3: Access the Airtable Database
- Access the Airtable Base using the personal access token.

Relevant Links:
    - https://airtable.com/create/tokens
    - https://airtable.com/developers/web/api/authentication
    - https://pyairtable.readthedocs.io/en/stable/getting-started.html

Step 4: Create a New Transaction Record
- Create a new record in the Transactions table.
    Date: Enter the date and time the transaction occurred.
    Description: Provide a brief, clear description of the transaction.
    Amount: Input the transaction amount.
    Account: Link to the account associated with the transaction.
    Type: Select whether the transaction is a debit or credit.

Step 5: Create a Journal Entry and Link the Transactions
- Create a new record in the Journals table.
    Name: Describe the journal entry.
    Transactions: Link to the transactions that make up the journal entry.


Step 6: Review for Accuracy
- Check Entries: Ensure that all the information entered is correct and
that the debit and credit entries are accurately reflected. Gather any missing information.


Step 7: Confirm the Entry
- Communication: Confirm with the business owner that the transaction has been recorded
"""
