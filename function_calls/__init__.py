

import function_calls.weather_information as weather_information
from .executor import Executor

tool_map = {
    "weather_information": weather_information.weather_information
}

functions_references = dict()

functions_references.update(weather_information.func_references)