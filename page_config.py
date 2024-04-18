
import streamlit as st

def set_page_config():
    st.set_page_config(
    page_title='ChatGPT Replica',
    page_icon='🌅',
    layout="wide"
    )
    
    st.title('Chat')

    st.sidebar.title('Chat Sessions')