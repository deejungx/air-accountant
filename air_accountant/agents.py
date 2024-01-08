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
    human_input_mode="ALWAYS",
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
        "record_transactions": record_bulk_transaction,
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
