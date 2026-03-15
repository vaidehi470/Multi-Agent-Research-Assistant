# from crewai_tools import DuckDuckGoSearchTool
# from crewai_tools.tools.duckduckgo_search_tool import DuckDuckGoSearchTool

# def get_search_tool():
#     return DuckDuckGoSearchTool()

# import crewai_tools
# print(dir(crewai_tools))

from crewai_tools import SerperDevTool

def get_search_tool():
    return SerperDevTool()