import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

class ChatLLM:
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        self.endpoint = "https://openrouter.ai/api/v1/chat/completions"
        # self.model = "deepseek/deepseek-chat-v3-0324:free"
        self.model="deepseek/deepseek-r1-distill-llama-70b:free"

    def query(self, prompt: str) -> str:
        response = requests.post(
            url=self.endpoint,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "model": self.model,
                "messages": [{"role": "user", "content": prompt}]
            })
        )
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content'].strip()
        else:
            raise RuntimeError(f"LLM API Error {response.status_code}: {response.text}")
