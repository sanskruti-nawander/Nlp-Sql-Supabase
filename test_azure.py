import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

print("KEY:", "SET" if os.getenv("AZURE_OPENAI_API_KEY") else "MISSING")
print("ENDPOINT:", os.getenv("AZURE_OPENAI_ENDPOINT"))
print("DEPLOYMENT:", os.getenv("AZURE_DEPLOYMENT_NAME"))

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version="2024-02-01"
)

response = client.chat.completions.create(
    model=os.getenv("AZURE_DEPLOYMENT_NAME"),
    messages=[{"role": "user", "content": "Say hello"}],
)

print("Azure response:", response.choices[0].message.content)
