import streamlit as st
from llm_chains import load_normal_chain
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from utils import load_config, save_chat_history_json,get_timestamp, load_chat_history_json
from page_config import set_page_config
import os

config = load_config()

def load_chain(chat_history):
    return load_normal_chain(chat_history)

def save_chat_history():
    if st.session_state.history != []:
        if st.session_state.session_key == 'new_session':
            st.session_state.new_session_key = get_timestamp() + '.json'
            save_chat_history_json(st.session_state.history, config['chat_history_path'] + st.session_state.new_session_key)
        else:
            save_chat_history_json(st.session_state.history, config['chat_history_path'] + st.session_state.session_key)

def track_index():
    st.session_state.session_index_tracker = st.session_state.session_key
    
def main():
    set_page_config()
    chat_container = st.container()
    chat_sessions = ['new_session'] + os.listdir(config['chat_history_path'])
    
    if 'conn' not in st.session_state:
        st.session_state.new_session_key = None
        st.session_state.session_index_tracker = "new_session"
        st.session_state.session_key = "new_session"
        st.session_state.conn = "" # for the moment
        
    if st.session_state.session_key == "new_session" and st.session_state.new_session_key != None:
        st.session_state.session_index_tracker = st.session_state.new_session_key
        st.session_state.new_session_key = None
    
    index = chat_sessions.index(st.session_state.session_index_tracker)
    st.sidebar.selectbox('Select a chat session', chat_sessions, key='session_key', index=index, on_change=track_index )
    
    if st.session_state.session_key != 'new_session':
        st.session_state.history = load_chat_history_json(config['chat_history_path'] + st.session_state.session_key)
    else:
        st.session_state.history = []
    
    chat_history = StreamlitChatMessageHistory(key='history')
    llm_chain = load_chain(chat_history)
    
    user_input = st.chat_input("Type your message here", key="user_input")
    
    if user_input:

        llm_response = llm_chain.run(user_input)
    
    if chat_history.messages != []:
        with chat_container:
            for message in chat_history.messages:
                st.chat_message(message.type).write(message.content)
    
    save_chat_history()
    
if __name__ == "__main__":
    main()
    