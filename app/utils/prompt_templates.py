SCHEMA = """
TABLE customers (
  realid TEXT PRIMARY KEY,
  name TEXT,
  phone TEXT,
  gender TEXT,
  bank TEXT,
  state TEXT,
  city TEXT,

  total_due NUMERIC,
  min_due NUMERIC,
  emi_avail BOOLEAN,
  emi_interested BOOLEAN,
  rewards_amt NUMERIC,
  utilization NUMERIC,
  days_since_bill NUMERIC,

  payment_status TEXT,
  default_segment TEXT,
  risk_segement TEXT,
  cust_del_segment TEXT,
  customer_sentiment TEXT,

  ptp_flagged BOOLEAN,
  rtp_flagged BOOLEAN,
  dispute_flagged BOOLEAN,
  escalation BOOLEAN,
  next_best_action TEXT,

  call_connected BOOLEAN,
  call_successful BOOLEAN,
  campaign_id TEXT,
  channel TEXT
);

TABLE call_logs (
  call_id UUID PRIMARY KEY,
  realid TEXT REFERENCES customers(realid),

  attempt_date DATE,
  attempt_time TIME,
  attempt_number NUMERIC,
  call_duration INTERVAL,
  call_cost NUMERIC,

  call_success BOOLEAN,
  call_end_reason TEXT,
  call_connected BOOLEAN,

  customer_sentiment TEXT,
  call_summary TEXT,

  ptp_captured BOOLEAN,
  ptp_amount TEXT,
  ptp_date TEXT,
  emi_interested BOOLEAN,
  waiver_interested BOOLEAN,
  dispute_flagged BOOLEAN,
  rtp_flagged BOOLEAN,
  escalation BOOLEAN,
  next_best_action TEXT
);
"""

SQL_PROMPT = f"""
You are a senior PostgreSQL data analyst.

STRICT RULES:
- Use ONLY the tables and columns in the schema
- customers.realid joins with call_logs.realid
- SELECT queries only
- NO SELECT *
- Return valid PostgreSQL SQL
- NO explanation

Schema:
{SCHEMA}

User Question:
{{query}}
"""
