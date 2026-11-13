import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# Load settings from the .env file
load_dotenv()

st.set_page_config(
    page_title="My AI Personal Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 My AI Personal Assistant")
st.caption("Version 1 — AI chat assistant")

api_key = os.getenv("OPENAI_API_KEY")
model_name = os.getenv("OPENAI_MODEL", "gpt-6-astra")

if not api_key:
    st.warning(
        "Open the project folder, create a file named .env, "
        "and add your OpenAI API key. See README.md for instructions."
    )
    st.stop()

client = OpenAI(api_key=api_key)

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("Settings")
    st.write(f"Model: `{model_name}`")
    if st.button("Clear conversation"):
        st.session_state.messages = []
        st.rerun()
    st.caption("Your chat history is kept in this browser session only.")

st.markdown(
    "Ask me questions, plan your day, draft messages, "
    "or get help understanding documents and spreadsheets."
)

# Show earlier messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept a new question
user_text = st.chat_input("Type your message here...")

if user_text:
    st.session_state.messages.append(
        {"role": "user", "content": user_text}
    )

    with st.chat_message("user"):
        st.markdown(user_text)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.responses.create(
                    model=model_name,
                    instructions=(
                        "You are a helpful personal assistant. "
                        "Give clear, practical answers. "
                        "When explaining technical topics, use beginner-friendly steps. "
                        "Do not claim to have performed actions you have not performed."
                    ),
                    input=st.session_state.messages,
                )
                answer = response.output_text
                st.markdown(answer)

                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )
            except Exception as error:
                st.error(
                    "I could not contact the AI service. "
                    "Check your internet connection, API key, API account billing, "
                    "and model name. Technical detail: " + str(error)
                )
