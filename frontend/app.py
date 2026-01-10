import streamlit as st
import requests

# =========================
# CONFIG
# =========================
BACKEND_API_URL = "https://nlp-sql-supabase.onrender.com/query"

st.set_page_config(
    page_title="NLP → SQL Chatbot",
    page_icon="🧠",
    layout="wide"
)

# =========================
# SESSION STATE
# =========================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# =========================
# SIDEBAR – QUERY HISTORY
# =========================
st.sidebar.title("🗂 Query History")

if len(st.session_state.chat_history) == 0:
    st.sidebar.info("No queries yet.")
else:
    for i, chat in enumerate(reversed(st.session_state.chat_history)):
        st.sidebar.markdown(f"**{len(st.session_state.chat_history)-i}.** {chat['query']}")

st.sidebar.markdown("---")
if st.sidebar.button("🧹 Clear History"):
    st.session_state.chat_history = []
    st.rerun()

# =========================
# MAIN UI
# =========================
st.title("🧠 NLP → SQL Analytics Chat")
st.caption("Ask business questions in plain English and get answers from Supabase")

# Chat display
for chat in st.session_state.chat_history:
    with st.chat_message("user"):
        st.write(chat["query"])
    with st.chat_message("assistant"):
        st.markdown(f"**Answer:** {chat['answer']}")
        with st.expander("Generated SQL"):
            st.code(chat["sql"], language="sql")
        with st.expander("Raw Result"):
            st.json(chat["result"])

# =========================
# INPUT BOX
# =========================
user_query = st.chat_input("Ask something like: 'Show unpaid customers from Mumbai'")

# =========================
# API CALL
# =========================
if user_query:
    with st.chat_message("user"):
        st.write(user_query)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    BACKEND_API_URL,
                    headers={"Content-Type": "application/json"},
                    json={"query": user_query},
                    timeout=60
                )

                if response.status_code == 200:
                    data = response.json()

                    answer = data.get("answer", "No answer")
                    sql = data.get("sql", "")
                    result = data.get("result", {})

                    st.markdown(f"**Answer:** {answer}")

                    with st.expander("Generated SQL"):
                        st.code(sql, language="sql")

                    with st.expander("Raw Result"):
                        st.json(result)

                    # Save to history
                    st.session_state.chat_history.append({
                        "query": user_query,
                        "answer": answer,
                        "sql": sql,
                        "result": result
                    })

                else:
                    st.error("Backend error")
                    st.code(response.text)

            except Exception as e:
                st.error("Failed to connect to backend")
                st.code(str(e))
