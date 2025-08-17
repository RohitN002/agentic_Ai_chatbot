from typing_extensions import TypedDict,list 
from langgraph.graph.message import add_messages
from typing import Annotated

class State(TypedDict):
    messages : Annotated[list, add_messages]