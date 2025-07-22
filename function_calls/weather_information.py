from bs4 import BeautifulSoup
import requests
from langchain.tools import tool
from langchain_core.utils.function_calling import convert_to_openai_function
from datetime import datetime

@tool
def get_weather(city_name: str, datetime: datetime):
    """
    Gets the weather information in a city of a given date and time.
    
    Parameters:
    ----------
    city_name: str
        The name of the city in which we require the weather information.

    datetime: datetime
        Date time of the requested time.

    Returns:
    -------
    str
        Weather information in details.
    """
    return f"Weather in {city_name} is heavily cloudy."

func_references = {"get_weather": get_weather}

registry = {
    f.name : convert_to_openai_function(f, strict=True) for f in func_references.values()
}