import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from app.prompts import SQL_PROMPT

def get_azure_client():
    load_dotenv()  # ensures env is loaded in subprocesses
    return AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_version="2024-02-01"
    )

def generate_sql(user_query: str) -> str:
    client = get_azure_client()

    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        messages=[{"role": "user", "content": SQL_PROMPT.format(query=user_query)}],
        temperature=0
    )

    return response.choices[0].message.content.strip()
