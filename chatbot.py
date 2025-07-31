import openai
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

# ⛔ IMPORTANT: Paste your OpenAI API key here
openai.api_key = sk - proj - uk41eDE3uQn0Ur6ZNcm5_IXQAqiTun5T6N6v8RZTZn1eoxqN - j5tLUUGrP6tXV5jvo6P6ws525T3BlbkFJdlypElEEdo_rfX6_hSobTqQFzLvxaoDOrqh6QBuf7STnZPssmM31_mUUkDc31iLE2aYZXnip4A


def ask_chatbot(user_input):
  chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3)

  messages = [
      HumanMessage(
          content=
          f"You are a helpful assistant trained to answer questions about cybersecurity awareness. Be clear, friendly, and concise.\n\nQuestion: {user_input}"
      )
  ]

  response = chat(messages)
  return response.content
