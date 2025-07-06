from bs4 import BeautifulSoup
import requests
from langchain.tools import tool
from langchain_core.utils.function_calling import convert_to_openai_function
from datetime import datetime

@tool
def graph_search(query):
    """
    Search in a personalized knowledge graph given the query. The knowledge graph is about the User's personal 
    relations and daily life. 
    
    Parameters:
    ----------
    query: str
        The query about relationships, entities, and temporal facts about User's life

    Returns:
    -------
    str
        Answer to the given query.
    """
    return f"GRAPH"

func_references = {"graph_search": graph_search}

weather_information = {"function_registry": {
    f.name : convert_to_openai_function(f, strict=True) for f in func_references.values()
}}