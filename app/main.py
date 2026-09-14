import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# Sync Streamlit Cloud secrets to environment variables if available
try:
    if hasattr(st, "secrets"):
        for key in ["GROQ_API_KEY", "GROQ_MODEL"]:
            if key in st.secrets:
                os.environ[key] = str(st.secrets[key])
except Exception:
    pass

from faq import ingest_faq_data, faq_chain
from sql import sql_chain
from smalltalk import talk
from pathlib import Path
from router import router

faqs_path = Path(__file__).parent / "resources/faq_data.csv"
ingest_faq_data(faqs_path)


def ask(query):
    try:
        route = router(query).name
        if route == 'faq':
            return faq_chain(query)
        elif route == 'sql':
            return sql_chain(query)
        elif route == 'small_talk':
            return talk(query)
        else:
            return f"Route {route} not implemented yet"
    except Exception as e:
        return f"Sorry, an error occurred while processing your request: {str(e)}"

st.title("E-commerce Bot")

query = st.chat_input("Write your query")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

if query:
    with st.chat_message("user"):
        st.markdown(query)
    st.session_state.messages.append({"role":"user", "content":query})

    response = ask(query)
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})


