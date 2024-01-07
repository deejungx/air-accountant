from dotenv import load_dotenv
import os

from air_accountant import create_api_connection

load_dotenv()


DEFAULT_ACCOUNTS = [
    {
        "name": "Cash",
        "type": "Asset",
        "description": "Holds the value of the company's cash on hand and in the bank.",
    },
    {
        "name": "Accounts Receivable",
        "type": "Asset",
        "description": "Represents money owed to the company by customers for goods or services delivered.",
    },
    {
        "name": "Inventory",
        "type": "Asset",
        "description": "Represents the cost of goods available for sale.",
    },
    {
        "name": "Prepaid Expenses",
        "type": "Asset",
        "description": "Payments made for expenses that will provide benefits over multiple periods.",
    },
    {
        "name": "Property, Plant, and Equipment",
        "type": "Asset",
        "description": "Represents the company's long-term assets like buildings and machinery.",
    },
    {
        "name": "Accounts Payable",
        "type": "Liability",
        "description": "Represents money the company owes to suppliers or vendors.",
    },
    {
        "name": "Accrued Liabilities",
        "type": "Liability",
        "description": "Expenses that have been incurred but not yet paid.",
    },
    {
        "name": "Loans Payable",
        "type": "Liability",
        "description": "Represents the principal amount of loans that are payable.",
    },
    {
        "name": "Unearned Revenue",
        "type": "Liability",
        "description": "Money received for goods or services that have not yet been delivered.",
    },
    {
        "name": "Capital",
        "type": "Equity",
        "description": "Represents the owner's investment in the business.",
    },
    {
        "name": "Retained Earnings",
        "type": "Equity",
        "description": "Earnings retained in the company to be used for business growth.",
    },
    {
        "name": "Sales Revenue",
        "type": "Revenue",
        "description": "Income from the sale of goods or services.",
    },
    {
        "name": "Service Revenue",
        "type": "Revenue",
        "description": "Income from services provided to customers.",
    },
    {
        "name": "Interest Income",
        "type": "Revenue",
        "description": "Income earned from investments.",
    },
    {
        "name": "Cost of Goods Sold",
        "type": "Expense",
        "description": "Direct costs attributable to the production of goods sold.",
    },
    {
        "name": "Salaries and Wages",
        "type": "Expense",
        "description": "Total payments made to employees for their services.",
    },
    {
        "name": "Rent Expense",
        "type": "Expense",
        "description": "Cost incurred for property used by the company.",
    },
    {
        "name": "Utilities",
        "type": "Expense",
        "description": "Cost of utilities used by the company like electricity, water, etc.",
    },
    {
        "name": "Insurance",
        "type": "Expense",
        "description": "Premiums paid for various insurance policies.",
    },
    {
        "name": "Depreciation",
        "type": "Expense",
        "description": "Allocation of the cost of tangible assets over their useful lives.",
    },
    {
        "name": "Marketing and Advertising",
        "type": "Expense",
        "description": "Costs associated with promoting the company and its products or services.",
    },
]


def initialize_accounts():
    """
    Initialize the Chart of Accounts with default accounts.
    """
    api = create_api_connection()
    base_id = os.getenv("AIRTABLE_BASE_ID")
    table_name = os.getenv("ACCOUNTS_TABLE_ID")
    accounts_table = api.table(base_id=base_id, table_name=table_name)
    accounts = accounts_table.all()  # get all records from the table
    if len(accounts) == 0:
        accounts_table.batch_create(DEFAULT_ACCOUNTS)
        print("Default accounts created.")
    else:
        print("Default accounts already exist.")


initialize_accounts()
