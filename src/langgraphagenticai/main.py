import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit

def load_langgraph_agnticai_app():

    ui= LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()

    if not user_input:
        st.error("Error : FAILED TO LOAD USER INPUT FROM THE UI")
        return

    user_message= st.chat_input("Enter yuur message  here")    

   if user_message:
    try:
        obj_llm_config=GroqLLM(user_controls_input=user_input)
        model=obj_llm_config.get_ll_model()
        if not model:
            st.error("LLM nodel could not be initialized ")
        usercase = user_input.get("selected_usecase")
        if not usecase:
            st.error("Error: no usecase selected")
            return 
        graph_builder=GraphBuilder(model)
        try:
            graph= graph_builder.setup_graph(usecase)
            DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()
        except Exception as e:
            st.error(f"Error graph setup failed -{e}") 
            return

        except Exception as e:      
            st.error(f"Error : Graph setup failed {e}")