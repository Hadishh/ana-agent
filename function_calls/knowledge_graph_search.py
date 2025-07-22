from bs4 import BeautifulSoup
import requests
from langchain.tools import tool
from langchain_core.utils.function_calling import convert_to_openai_function
from datetime import datetime

@tool
def graph_search(query):
    """
    Searches a personalized knowledge graph for information related to the user's personal relationships,
    daily life, and specific events or entities within their personal context. This function leverages
    a unique knowledge graph tailored to the individual user, allowing for highly relevant and
    context-aware responses to queries about their personal world.

    Parameters:
    ----------
    query: str
        The natural language query text to be searched within the personalized knowledge graph.
        Examples include "When is Mom's birthday?", "What did I do last Tuesday?",
        "Where did I put my keys?", or "Who is Sarah's husband?".

    Returns:
    -------
    str
        A comprehensive and contextually relevant answer to the given query, extracted from
        the personalized knowledge graph. If the information is not found, a suitable
        message indicating that will be returned.
    """
    return f"GRAPH"

func_references = {"graph_search": graph_search}

registry = {
    f.name : convert_to_openai_function(f, strict=True) for f in func_references.values()
}