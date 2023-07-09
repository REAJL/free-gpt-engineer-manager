from __future__ import annotations
import logging, requests, json

logger = logging.getLogger(__name__)

class AI:
    url = "https://gpt4.xunika.uk"
    arguments = "/api/openai/v1/chat/completions"
    headers = {"Content-Type": "application/json"}

    def __init__(self, model="gpt-3.5-turbo", temperature=0.9):
        self.temperature = temperature
        if model!="gpt-3.5-turbo":
            print(f"Model {model} not available, sorry. Currently you use GPT-3.5-Turbo")
            self.model = "gpt-3.5-turbo"

    def process_text(self, text):
        data = text.text
        data_json = json.loads(data)
        if "choices" in data_json:
            choices = data_json["choices"]
            for choice in choices:
                if "message" in choice and "content" in choice["message"]:
                    content = choice["message"]["content"]
                    return content
                else:
                    return "Error. GPT-3.5-Turbo don't work."
        else:
            return "Error. GPT-3.5-Turbo don't work."


    def call(self, messages, temperature) -> str:
        data = {
            "model": "gpt-3.5-turbo",
            "temperature": temperature,
            "messages": messages
        }

        endpoint = self.url + self.arguments
        with requests.post(url=endpoint, headers=self.headers, json=data) as response:
            msg = self.process_text(response)
            return msg

    def start(self, system, user):
        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ]

        return self.next(messages)

    def fsystem(self, msg):
        return {"role": "system", "content": msg}

    def fuser(self, msg):
        return {"role": "user", "content": msg}

    def fassistant(self, msg):
        return {"role": "assistant", "content": msg}

    def next(self, messages: list[dict[str, str]], prompt=None):
        if prompt:
            messages += [{"role": "user", "content": prompt}]

        logger.debug(f"Creating a new chat completion: {messages}")
        response = self.call(
            messages=messages,
            temperature=self.temperature,
        )

        print(response)
        print()
        messages += [{"role": "assistant", "content": response}]
        logger.debug(f"Chat completion finished: {messages}")
        return messages

