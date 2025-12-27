from openai import AzureOpenAI
from app.core.config import settings
from app.utils.prompt_templates import SQL_PROMPT

client = AzureOpenAI(
    api_key=settings.AZURE_OPENAI_KEY,
    azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
    api_version="2024-02-01"
)

def generate_sql(user_query: str) -> str:
    response = client.chat.completions.create(
        model=settings.AZURE_DEPLOYMENT_NAME,
        messages=[
            {"role": "user", "content": SQL_PROMPT.format(query=user_query)}
        ],
        temperature=0
    )
    return response.choices[0].message.content.strip()
