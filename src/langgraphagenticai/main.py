import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI


def load_langgraph_agnticai_app():

    ui= LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()

    if not user_input:
        st.error("Error : FAILED TO LOAD USER INPUT FROM THE UI")
        return

    user_messages= st.chat_input("Enter yuur message here")    