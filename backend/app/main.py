from fastapi import FastAPI
from dotenv import load_dotenv
from app.routes import router

load_dotenv()  # critical for uvicorn reload on Windows

app = FastAPI(
    title="Supabase NL Query Engine",
    description="Query customers and call logs using natural language",
    version="1.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {"status": "API is running"}

