import streamlit as st
import requests
import os

API_URL = os.environ.get('LEGAL_API_URL', 'http://localhost:8000/query')

st.title("Legal Assistant Bot (Skeleton)")
q = st.text_area("Question", height=100)
ctx = st.text_area("Context (optional)", height=150)

if st.button("Ask"):
    if not q.strip():
        st.warning("Please write a question.")
    else:
        resp = requests.post(API_URL, json={'question': q, 'context': ctx})
        if resp.ok:
            st.markdown('**Answer:**')
            st.write(resp.json().get('answer'))
        else:
            st.error(f"API error: {resp.status_code}")
