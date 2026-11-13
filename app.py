import os
import streamlit as st
from google import genai

# Page setup
st.set_page_config(page_title="My AI Personal Assistant", page_icon="🤖")
st.title("🤖 My AI Personal Assistant")

# Load API key from Streamlit Secrets or local environment variables
api_key = st.secrets.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")

if not api_key:
    st.warning("GEMINI_API_KEY not found. Please add it to Streamlit Secrets or your .env file.")
    st.stop()

# Initialize the Gemini client
client = genai.Client(api_key=api_key)

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input
if prompt := st.chat_input("Ask me anything..."):
    # Add user message to history and display it
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response from Gemini
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt,
            )
            st.markdown(response.text)
            
    # Save assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": response.text})
