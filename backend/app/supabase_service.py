import os
import json
from dotenv import load_dotenv
from supabase import create_client
from decimal import Decimal
from datetime import date, datetime

def get_supabase_client():
    load_dotenv()
    return create_client(
        os.getenv("SUPABASE_URL"),
        os.getenv("SUPABASE_SERVICE_ROLE_KEY")
    )

def sanitize_sql(sql: str) -> str:
    sql = sql.strip()

    if sql.startswith("```"):
        sql = sql.replace("```sql", "").replace("```", "").strip()

    sql = sql.split(";")[0].strip()
    return sql

def make_json_safe(obj):
    """
    Converts non-JSON-serializable objects to safe formats
    """
    if isinstance(obj, Decimal):
        return float(obj)
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    return obj

def execute_sql(sql: str):
    supabase = get_supabase_client()
    clean_sql = sanitize_sql(sql)

    response = supabase.rpc(
        "execute_sql",
        {"query": clean_sql}
    ).execute()

    # Convert all rows to JSON-safe
    safe_result = json.loads(
        json.dumps(response.data or [], default=make_json_safe)
    )

    return safe_result

def store_insight(user_query, sql, result, answer):
    supabase = get_supabase_client()

    # Ensure result is JSON-safe
    safe_result = json.loads(
        json.dumps(result, default=make_json_safe)
    )

    supabase.table("query_insights").insert({
        "user_query": user_query,
        "generated_sql": sql,
        "result": safe_result,
        "answer": answer
    }).execute()
