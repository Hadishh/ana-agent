from dotenv import load_dotenv
load_dotenv()

from agents import MAIN_AGENT
from function_calls import tool_map, Executor, functions_references
agent = MAIN_AGENT

curr_exec = Executor(
    tool_registry=tool_map, 
    action_registry={"function_registry": {}}, 
    funcs_ref=functions_references
)


agent.generate_functions_and_responses(
    tool_registry=tool_map, 
    action_registry={"function_registry": {}}, 
    persona=None, 
    dialogue=None, 
    executor=curr_exec)

