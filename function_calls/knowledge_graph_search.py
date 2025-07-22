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

    When referencing the user within responses, use their specific name instead of coreferences like "I" or "my".
    For example, if the user's name is "Alex", instead of "What did I do last Tuesday?", the query would be
    interpreted in the context of "What did Alex do last Tuesday?". Avoid using coreferences
    without explicitly mentioning the user's name.

    Parameters:
    ----------
    query: str
        The natural language query text to be searched within the personalized knowledge graph.

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