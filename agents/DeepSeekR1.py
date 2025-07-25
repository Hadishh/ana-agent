import os
from datetime import datetime
import copy
from openai import OpenAI

from agents.agent_base import Agent
from agents.utils import read_file


class DeepSeekAgent(Agent):
    def __load_llm_client(self):
        self.llm_client = OpenAI(
            base_url=os.getenv("OPENAI_BASE_URL"),
            api_key=os.getenv("OPENAI_API_KEY"),
        )

    def __init__(self, model_name="deepseek-r1-32b"):
        super().__init__()
        self.__load_llm_client()
        self.model_name= model_name

        self.MAX_NEW_TOKENS = 16384
        self.temperature= 0.6
    
    def generate_functions_and_responses(self, tool_registry, action_registry, persona, dialogue, executor):
        functions = self._create_message_for_functions(tool_registry, action_registry, dialogue, persona)
        res = self.llm_client.completions.create(
            model=self.model_name,
            prompt=functions,
            max_tokens=self.MAX_NEW_TOKENS,
            temperature=0.6
        )

        items = res.choices[0].text.split("</think>")[-1].split("\n")
        final_functions = []
        res_item = {}
        for item in items:
            item = item.lower()
            if "function name: " in item:
                if "name" in res_item:
                    final_functions.append(copy.deepcopy(res_item))
                    res_item = {}
                res_item["name"] = item.replace("function name: ", "").split(",")[0]
                res_item["parameters"] = {}
            elif "argument name: " in item:
                arg_name = ""
                arg_val = ""
                if "value: " in item:
                    arg_name = item.split("value: ")[0].replace("argument name: ", "").split(",")[0]
                    arg_val = item.split("value: ")[1]

                if arg_name != "":
                    if not "parameters" in res_item:
                        res_item["parameters"] = {}
                    res_item["parameters"][arg_name] = arg_val
                    
        if "name" in res_item:
            final_functions.append(res_item)

        function_results = executor.execute(final_functions)

        dialogue_prompt = self._create_dialogue_message(persona, dialogue, function_results)
        response = self.llm_client.completions.create(
            model=self.model_name,
            prompt=dialogue_prompt,
            max_tokens=self.MAX_NEW_TOKENS,
            temperature=0.6
        )

        items = response.choices[0].text.split("</think>")[-1].split("\n")

        print(items)

    def _create_message_for_functions(self, tool_functions, action_functions, dialogue, context):
        prompt = read_file("./prompts/function_prompt.txt")

        # Prepare function information by concatenating all function names and docstrings. 
        function_information = []
        for tool_name in tool_functions['function_registry'].keys():
            tool_ = tool_functions['function_registry'][tool_name]
            tool_prompt = (
                "# Function Name: {}\n"
                "# Function Docstring: {}\n"
            ).format(tool_['name'], tool_['description'])
            function_information.append(tool_prompt)
        for action_name in action_functions['function_registry'].keys():
            action_ = action_functions['function_registry'][action_name]
            action_prompt = (
                "# Function Name: {}\n"
                "# Function Docstring: {}\n"
            ).format(action_['name'], action_['description'])
            function_information.append(action_prompt)
        function_information_agg = '\n'.join(function_information)

        # history = dialogue[-11:]

        context = f"User's Name: Hadi\nUser's Age: 26\nUser's City: Edmonton\nCurrent time:{str(datetime.now())}"
        history = [
            {"id": 1, "text": "Hi ANA!"},
            {"id": 1, "text": "Hi Hadi how are you today?"},
            {"id": 1, "text": "My neighbor is coming for a visit!"},
        ]
        input_text = history[-1]["text"]

        prompt = prompt.replace("{functions}", function_information_agg) \
                        .replace("{context}", context) \
                        .replace("{history}", "\n".join([h["text"] for h in history]))
        
        return prompt
    
    def _create_dialogue_message(self, context, history, function_results):
        context = f"User's Name: Hadi\nUser's Age: 26\nUser's City: Edmonton\nCurrent time:{str(datetime.now())}"
        history = [
            {"id": 1, "text": "Hi ANA!"},
            {"id": 1, "text": "Hi Hadi how are you today?"},
            {"id": 1, "text": "good, planning for a walk, how is the weather today?"},
        ]
        prompt = read_file("prompts/messages_prompt.txt")

        funciton_outputs = ""
        for result in function_results:
            result = function_results[result]
            funciton_outputs = funciton_outputs + f"Function {result['name']} Output:\n{result['output']}\n"
        
        prompt = prompt.replace("{external_kg}", funciton_outputs) \
                        .replace("{user_info}", context) \
                        .replace("{history}", "\n".join([h["text"] for h in history]))

        return prompt