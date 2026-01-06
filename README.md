🧠 Supabase Natural Language Query Engine

This project enables users to query Supabase databases using natural language.
It converts user queries into safe SQL, executes them on Supabase, and stores the query, SQL, and results for analytics and auditing.

🚀 Project Overview

The system allows business and operations teams to ask questions like:

“List high risk unpaid customers from Mumbai”

and receive accurate results without writing SQL.

Key Capabilities

Natural Language → SQL using Azure OpenAI

Secure query execution using Supabase RPC

Queries restricted to SELECT-only

Results stored in query_insights table

Swagger UI for easy testing

🧩 Tech Stack

Backend: FastAPI

LLM: Azure OpenAI (GPT-4o)

Database: Supabase (PostgreSQL)

Execution Layer: Supabase RPC

API Docs: Swagger (OpenAPI)

🗂️ Database Tables Used
1️⃣ Customers (PDD Recovery)

Key attributes:

realid

name

city, state

total_due

payment_status

risk_segement

ptp_flagged, rtp_flagged

dispute_flagged

escalation

2️⃣ Call Logs (PDM)

Key attributes:

call_id

realid

attempt_date

attempt_number

call_success

ptp_captured

emi_interested

dispute_flagged

escalation

customer_sentiment

3️⃣ Query Insights (Analytics)

Stores:

User query

Generated SQL

Query result (JSONB)

Natural language answer

Timestamp

🔐 Security & Guardrails

Only SELECT queries are allowed

No INSERT / UPDATE / DELETE

Queries must start with SELECT

SQL is sanitized before execution

Supabase RPC enforces database safety

🧪 Supported Natural Language Queries

Below is a list of example queries that the system supports.
All of these can be directly executed via Swagger UI.

📊 Customer Recovery Queries

List high risk unpaid customers from Mumbai

Show customers with total due greater than 50,000

Find customers with payment status unpaid

List customers flagged for escalation

Show customers with disputes raised

Find customers with RTP flagged

List customers eligible for EMI

Show customers with utilization above 80 percent

List customers grouped by risk segment

Show top 10 customers by total due

🌍 Geography-Based Queries

Count unpaid customers by city

List customers from Maharashtra

Show customers grouped by state

Find customers from Mumbai with high risk

Show total outstanding amount by city

📞 Call Log Queries

List customers whose calls were not successful

Show customers contacted more than 3 times

Find call attempts with escalation flagged

List customers who showed EMI interest during calls

Show customers with PTP captured

Find customers with dispute flagged during calls

Show customers with negative call sentiment

🔗 Combined Customer + Call Queries

List unpaid customers who were contacted but calls failed

Show high risk customers with negative call sentiment

Find customers contacted multiple times and still unpaid

Show customers with escalation in both customer and call logs

List customer name, city, and last call outcome

📈 Operational & Management Insights

Count total unpaid customers

Show percentage of successful calls

Find customers with highest call attempts

Show customers where next action is escalation

List customers not contacted yet

🧪 Edge Case & Data Quality Queries

List customers where city is null

Show customers with missing risk segment

Find call logs with missing sentiment

List customers with no call history

Show customers with zero call attempts

▶️ How to Run the Project
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn app.main:app --port 8001


Open Swagger UI:

http://127.0.0.1:8001/docs

🧪 Sample Request (Swagger)
{
  "query": "List high risk unpaid customers from Mumbai"
}

🧾 Sample Response
{
  "sql": "SELECT realid, name, total_due FROM customers WHERE city = 'Mumbai' AND payment_status = 'unpaid' AND risk_segement = 'High'",
  "result": [
    {
      "realid": "2948977442234041394",
      "name": "John Doe",
      "total_due": 75000.0
    }
  ],
  "answer": "There is 1 high-risk unpaid customer in Mumbai."
}

📌 Key Design Decisions

Supabase RPC used instead of direct DB connections

Query results stored for audit and analytics

JSONB used for efficient result storage

Prompt and sanitization layered for safety

🔮 Future Enhancements

Intent-based query routing

Query accuracy scoring

Role-based access control

Streamlit / Next.js UI

Dashboard over query_insights

👤 Author

Built as a real-world analytics and recovery intelligence system using modern GenAI and database best practices.
