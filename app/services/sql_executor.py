from sqlalchemy import create_engine, text
from app.core.config import settings

DATABASE_URL = settings.SUPABASE_URL.replace(
    "https://", "postgresql://"
) + f"?apikey={settings.SUPABASE_KEY}"

engine = create_engine(DATABASE_URL)

def execute_sql(sql: str):
    with engine.connect() as conn:
        result = conn.execute(text(sql))
        return [dict(row) for row in result]
