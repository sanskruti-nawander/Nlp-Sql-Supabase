from fastapi import APIRouter
from app.models.schemas import QueryRequest, QueryResponse
from app.services.azure_openai import generate_sql
from app.services.sql_executor import execute_sql
from app.services.response_formatter import format_response
from app.db.supabase_client import supabase

router = APIRouter()

@router.post("/query", response_model=QueryResponse)
def process_query(data: QueryRequest):
    sql = generate_sql(data.query)
    result = execute_sql(sql)
    answer = format_response(result, data.query)

    supabase.table("query_insights").insert({
        "user_query": data.query,
        "generated_sql": sql,
        "response": answer
    }).execute()

    return {"sql": sql, "answer": answer}
