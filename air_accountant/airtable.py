import logging
import os

from dotenv import load_dotenv
from pyairtable import Api


load_dotenv()  # load environment variables from .env file
logger = logging.getLogger(__name__)


def create_api_connection():
    """
    Create a connection to the Airtable API.
    """
    airtable_api_key = os.getenv("AIRTABLE_ACCESS_TOKEN")
    api = Api(api_key=airtable_api_key)  # create an API for connecting Airtable
    return api


def get_all_accounts():
    """
    Fetch all accounts from the Chart of Accounts.
    """
    api = create_api_connection()
    base_id = os.getenv("AIRTABLE_BASE_ID")
    table_name = os.getenv("ACCOUNTS_TABLE_ID")
    accounts_table = api.table(base_id=base_id, table_name=table_name)
    logger.debug(f"Fetching all accounts from table_id: {table_name}")
    result = accounts_table.all()  # get all records from the table
    logger.info(f"Fetched {len(result)} accounts")
    accounts = [
        {
            "id": acc["fields"]["acc_number"],
            "name": acc["fields"]["name"],
            "description": acc["fields"]["description"],
            "type": acc["fields"]["type"],
        }
        for acc in result
    ]
    return accounts


def record_transaction(date, description, amount, account_number, type):
    """
    Record a transaction to the Transactions table.
    """
    api = create_api_connection()
    base_id = os.getenv("AIRTABLE_BASE_ID")
    table_name = os.getenv("TRANSACTIONS_TABLE_ID")
    transactions_table = api.table(base_id=base_id, table_name=table_name)
    tx_result = transactions_table.create(
        {
            "date": date,
            "description": description,
            "amount": amount,
            "account": account_number,
            "type": type,
        }
    )
    return tx_result


def record_bulk_transaction(transactions):
    """
    Record a list of transactions to the Transactions table.
    """
    api = create_api_connection()
    base_id = os.getenv("AIRTABLE_BASE_ID")
    table_name = os.getenv("TRANSACTIONS_TABLE_ID")
    logger.debug(
        f"Recording transactions to table_id: {table_name}\n\ntransactions:\n\n{transactions}"
    )
    transactions_table = api.table(base_id=base_id, table_name=table_name)
    tx_result = transactions_table.batch_create(transactions)
    logger.info(f"Recorded {len(tx_result)} transactions")
    return tx_result


def record_journal_entry(name, date, transactions):
    """
    Record a journal entry to the Journal Entries table.
    """
    api = create_api_connection()
    base_id = os.getenv("AIRTABLE_BASE_ID")
    table_name = os.getenv("JOURNALS_TABLE_ID")
    journal_entries_table = api.table(base_id=base_id, table_name=table_name)
    je_result = journal_entries_table.create(
        {"name": name, "date": date, "transactions": transactions}
    )
    return je_result


def record_bulk_journal_entry(journal_entries):
    """
    Record a list of journal entries to the Journal Entries table.
    """
    api = create_api_connection()
    base_id = os.getenv("AIRTABLE_BASE_ID")
    table_name = os.getenv("JOURNALS_TABLE_ID")
    journal_entries_table = api.table(base_id=base_id, table_name=table_name)
    je_result = journal_entries_table.batch_create(journal_entries)
    return je_result
