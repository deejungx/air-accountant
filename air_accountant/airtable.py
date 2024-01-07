import os

from dotenv import load_dotenv
from pyairtable import Api


load_dotenv()  # load environment variables from .env file


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
    result = accounts_table.all()  # get all records from the table
    accounts = [
        {
            "name": acc["fields"]["name"],
            "description": acc["fields"]["description"],
            "type": acc["fields"]["type"],
        }
        for acc in result
    ]
    return accounts
