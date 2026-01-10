from fastapi import APIRouter
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from openai import AzureOpenAI

from app.openai_service import generate_sql
from app.supabase_service import execute_sql, store_insight

router = APIRouter()

class QueryRequest(BaseModel):
    query: str

def get_azure_client():
    load_dotenv()
    return AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_version="2024-02-01"
    )

@router.post("/query")
def query_data(data: QueryRequest):
    sql = generate_sql(data.query)
    result = execute_sql(sql)

    client = get_azure_client()
    summary_prompt = f"""
User Question:
{data.query}

SQL Result:
{result}

Give a clear business-friendly answer.
"""

    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        messages=[{"role": "user", "content": summary_prompt}],
        temperature=0.3
    )

    answer = response.choices[0].message.content.strip()

    store_insight(data.query, sql, result, answer)

    return {
        "sql": sql,
        "result": result,
        "answer": answer
    }
