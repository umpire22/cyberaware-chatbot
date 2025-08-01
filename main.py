# Check if OpenAI is installed
try:
  import openai
  print("✅ OpenAI module is available")
except ImportError:
  print("❌ OpenAI module is NOT installed")

from chatbot import ask_chatbot
import streamlit as st

# Your Streamlit app code follows...

import streamlit as st
from chatbot import ask_chatbot

st.set_page_config(page_title="CyberAware Bot", page_icon="🛡️")
st.title("🛡️ Cybersecurity Awareness Chatbot")
st.write(
    "Ask anything about cybersecurity—phishing, passwords, safe browsing, and more!"
)

user_input = st.text_input("Type your question here:")

if user_input:
  with st.spinner("Thinking..."):
    response = ask_chatbot(user_input)
  st.success("Here’s the answer:")
  st.markdown(response)
# Force rebuild on Streamlit Cloud
