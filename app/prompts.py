SCHEMA = """
TABLE customers (
  realid TEXT,
  name TEXT,
  city TEXT,
  state TEXT,
  total_due NUMERIC,
  payment_status TEXT,
  risk_segement TEXT,
  ptp_flagged BOOLEAN,
  rtp_flagged BOOLEAN,
  dispute_flagged BOOLEAN,
  escalation BOOLEAN
);

TABLE call_logs (
  call_id UUID,
  realid TEXT,
  attempt_date DATE,
  attempt_number NUMERIC,
  call_success BOOLEAN,
  ptp_captured BOOLEAN,
  emi_interested BOOLEAN,
  dispute_flagged BOOLEAN,
  escalation BOOLEAN,
  customer_sentiment TEXT
);
"""

SQL_PROMPT = f"""
You are a PostgreSQL expert.

Return ONLY a single SQL SELECT statement.
- Do not use markdown
- Do not add explanations
- Do not add semicolons
- The query MUST start with SELECT

Schema:
{SCHEMA}

User Question:
{{query}}
"""

