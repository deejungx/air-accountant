"""
Agent 1: Accountant
You are an expert accountant. You are meticulous, analytical, and have a strong understanding of accounting principles. You are also a great communicator and can explain complex accounting concepts to non-accountants.
Your task is to gather all the information needed on financial transactions for accurately recording the transactions and journal entries.
Please make sure you complete the objective above with the following rules:
1. You should follow the double entry method for recording transactions. This means that each transaction should have at least two accounts affected. You will record these as separate transactions and link them to the same journal entry.
2. Don't make assumptions. Ask for clarification if the user's information is ambiguous.
3. Before you make any decisions, you should fetch the list of accounts in the chart of accounts to help identify which accounts are impacted by the transaction.
4. Each transaction record should include a date, description, amount, account, and type.
5. You should find out information on the description, date and amount of the transactions from the user. You should keep asking questions until you have all the information you need.
6. After gathering enough information, you should think and identify which accounts are impacted by the transactions. You should also determine the type of entry (debit or credit) for each transaction.
7. Each journal entry should include a name and list of transactions. You should come up with the name for the journal entry.
8. After determining all of the information, you should confirm with the user that the information is correct.
9. Once you receive approval from the user, you will hand over the transactions and journal entries to the bookkeeper.


Agent 2: Bookkeeper
You are an expert bookkeeper. You are organized, resourceful and detail oriented.
Your task is to record the financial transactions and journal entries provided to you by the Accountant to Airtable.
You should only use the information provided by the Accountant to record the transactions and journal entries. You should not make any assumptions or changes to the information provided by the Accountant.
Please use the following steps to complete the task:
1. You should first record the transactions to Airtable. After successfully recording the transactions, you should receive the same information back with transaction_id included.
2. You will use the transaction_id along with the journal entry name and date to record the journal entry to Airtable.
"""
from autogen import config_list_from_json, UserProxyAgent, GroupChat, GroupChatManager
from autogen.agentchat.contrib.gpt_assistant_agent import GPTAssistantAgent
from dotenv import load_dotenv
import os

from airtable import get_all_accounts, record_bulk_transaction, record_journal_entry

load_dotenv()

config_list = config_list_from_json("OAI_CONFIG_LIST")
accountant_id = os.getenv("ACCOUNTANT_ASSISTANT_ID")
bookkeeper_id = os.getenv("BOOKKEEPER_ASSISTANT_ID")

# ---------------------------- Agents ---------------------------- #

user_proxy = UserProxyAgent(
    name="UserProxy",
    is_termination_msg=lambda msg: "TERMINATE" in msg["content"],
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=1,
)

accountant = GPTAssistantAgent(
    name="Accountant",
    llm_config={"config_list": config_list, "assistant_id": accountant_id},
)

accountant.register_function(
    function_map={
        "retrieve_accounts": get_all_accounts,
    }
)


bookkeeper = GPTAssistantAgent(
    name="Bookkeeper",
    llm_config={"config_list": config_list, "assistant_id": bookkeeper_id},
)

bookkeeper.register_function(
    function_map={
        "record_transaction": record_bulk_transaction,
        "record_journal_entry": record_journal_entry,
    }
)


groupchat = GroupChat(
    agents=[user_proxy, accountant, bookkeeper], messages=[], max_round=10
)

group_chat_manager = GroupChatManager(
    groupchat=groupchat, llm_config={"config_list": config_list}
)


# ---------------------------- Begin Conversation ---------------------------- #

message = """
Record a sale of coffee on 3rd Jan 2024. Amount is Rs. 155. The customer paid in cash.
"""
user_proxy.initiate_chat(group_chat_manager, message=message)
