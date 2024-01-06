import os

from dotenv import load_dotenv
from pyairtable import Api


load_dotenv()  # load environment variables from .env file

airtable_api_key = os.getenv("AIRTABLE_ACCESS_TOKEN")

api = Api(api_key=airtable_api_key)  # create an API for connecting Airtable

table = api.table(base_id="appbBLdsfMwHUL1jV", table_name="tblGdD4OLW15RCGD4")

tables = table.all()  # get all records from the table

print(tables)
