import copy
import re

class Executor: 
    """
        A wrapper for function calls. 
        It implements the function calls by calling `execute` in function_calls,
        and records the function call names and args for evaluation purposes. 
    
        Notes: 
            1. This executor is a sample one. It will only check whether the output matches the gold functions. 
               If it matches, we will return the gold return values. 
               It it does not match, it will return nothing. 
               However, in real evaluations, the executor will return adequate values even though it is not an exact match with gold functions. 
            2. Please do not try to tamper with attributes in the Executor. Doing so will lead to errors. 
    """
    def __init__(self, tool_registry, action_registry, funcs_ref, threshold=0.4):
        self.function_call_stats = []
        self.tool_registry = tool_registry
        self.action_registry = action_registry
        self.funcs_ref = funcs_ref
        self.threshold = 0.4
        # This is a temporary value. The value may be subject to change by the organizers. 
    
    def execute(self, function_list): 
        """
            Execute the list of functions by checking the gold functions.
            It will also record the function call names and args (for evaluation purposes). 
        """
        copy_functions = copy.deepcopy(function_list)
        results = {}
        for func_item in copy_functions:
            self.function_call_stats.append(copy.deepcopy(func_item))
            name = func_item["name"].strip()
            args = {k.strip(): v.strip() for k, v in func_item["parameters"].items()}

            if name in self.funcs_ref:
                func_output = self.funcs_ref[name].func(**args)
                results[f"{name}({args})"] = {"name": name, "output": func_output}
            
        return results
