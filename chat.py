import json
from openai import OpenAI
from register_tools import register_tools, dispatch, get_tools_list

class ChatGPT:
    def __init__(self, key, model, system_prompt='', temperature=1):
        self.key = key
        self.gpt = OpenAI(api_key=key)
        self.model = model
        self.temperature = temperature
        self.client = self.gpt.chat.completions
        self.chat_history = [
            {"role": "system", "content": system_prompt},
        ]
        self.available_functions = {}
        self.tools = None

    def ask(self, question):
        self.chat_history.append({
                "role": "user",
                "content": question,
            })
        response = self.request_from_gpt()

        response = self.deal_with_response(response)

        return response.choices[0].message

    def add_tool(self, func, description, schema):
        if not self.tools:
            self.tools = []
        self.tools.append({
            "type": "function",
            "function": {
                "name": func.__name__,
                "description": description,
                "parameters": schema,
            },
        })
        self.available_functions[func.__name__] = func

    def request_from_gpt(self):
        if self.tools:
            return self.client.create(
                model=self.model,
                messages=self.chat_history,
                tools=self.tools,
                # temperature=self.temperature,
            )
        else:
            return self.client.create(
                model=self.model,
                messages=self.chat_history,
            )

    def deal_with_response(self, response):
        self.chat_history.append(response.choices[0].message)
        tool_calls = response.choices[0].message.tool_calls

        if tool_calls:
            for tool_call in tool_calls:
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)

                self.call_function(tool_call.id, function_name, function_args)

            second_response = self.request_from_gpt()

            return self.deal_with_response(second_response)

        return response
    
    def call_function(self, id, function_name, function_args):
        function_to_call = self.available_functions[function_name]
        func_response = function_to_call(**function_args)

        self.chat_history.append({
            "role": "tool",
            "tool_call_id": id,
            "name": function_name,
            "content": func_response,
        })

        return
