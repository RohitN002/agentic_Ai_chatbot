import streamlit as st 
import os 
from src.langgraphagenticai.ui.streamlitui.uiconfigfile import config

class LoadStreamlitUI:
    def __init__(self):
        self.config=config()
        self.user_controls={}

    def  load_streamlit_ui(self):
        st.set_page_config(page_title="🤖"+self.config.get_page_title(), layout="wide")
        st.header("🤖"+self.config.get_page_title())

    with st.sidebar:
        llm_options=self.config.get_llm_options()
        usecase_options= self.config.get_usecase_options()

        if self.user_controls["selected_llm"]=='Groq':
            model_options=self.config.get_groq_model_options()
            self.user_controls["selected_groq_model"]= st.selectbox("Select Model", model_options)
            self.user_controls["GROQ_API_KEY"]=st.session_state["GROQ_API_KEY"]=st.text_input("API Key", type="password")

            if not self.user_controls["GROQ_API_KEY"]:
                st.warning("⚠️ please enter your groq api key to proceed")


         self.user_controls["selected_usecase"]=st.selectbox("select usecases", usecase_options)
    return self.user_controls              
