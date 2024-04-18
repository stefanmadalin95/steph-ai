import streamlit as st
from st_chat_message import message
import tmp.chain as chain
from datetime import datetime

st.set_page_config(
  page_title='ChatGPT Replica',
  page_icon='🌅',
  layout="wide"
)
st.title('Chat')

if "llm_chain" not in st.session_state:
    st.session_state.llm_chain = chain.create_llm_chain()

if "messages" not in st.session_state:
    st.session_state.messages = []

def append_state_messages(user_message, bot_message):
    st.session_state.messages.append({"user_message": user_message, "bot_message": bot_message})

def restore_history_messages():
    for history_message in st.session_state.messages:
        message(history_message["user_message"], is_user=True, key=str(datetime.now()))
        message(history_message["bot_message"], is_user=False,key=str(datetime.now()))

user_message = st.chat_input(placeholder="Type a message...")
if user_message:
    restore_history_messages()
    output = st.session_state.llm_chain.predict(human_input=user_message)
    message(user_message, is_user=True, key="user_message")
    message(output, is_user=False, key="bot_message")
    append_state_messages(user_message, output)
        

    