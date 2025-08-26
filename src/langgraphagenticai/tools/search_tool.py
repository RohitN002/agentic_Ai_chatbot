from lanchain_community.tools.tavily_search import TavilySearchReesult
from langgraph.prebuilt import ToolNode

def get_tools():
    tools=[TavilySearchReesult(max_results=2)]
    return tools

def create_tool_node(tool):
    return ToolNode(tool)    