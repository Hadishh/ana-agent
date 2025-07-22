

import function_calls.weather_information as weather_information
import function_calls.knowledge_graph_search as knowledge_graph_search
from .executor import Executor

tool_map = {
    "function_registry": {**knowledge_graph_search.registry, **weather_information.registry}
}

functions_references = dict()

functions_references.update(weather_information.func_references)
functions_references.update(knowledge_graph_search.func_references)