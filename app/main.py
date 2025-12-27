from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Azure NL → SQL → Supabase")

app.include_router(router)
