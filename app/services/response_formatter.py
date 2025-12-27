from openai import AzureOpenAI
from app.core.config import settings

client = AzureOpenAI(
    api_key=settings.AZURE_OPENAI_KEY,
    azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
    api_version="2024-02-01"
)

def format_response(result, question):
    prompt = f"""
User Question:
{question}

SQL Result:
{result}

Generate a clear, concise business-friendly answer.
"""

    response = client.chat.completions.create(
        model=settings.AZURE_DEPLOYMENT_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content.strip()
