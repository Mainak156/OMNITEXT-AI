import os
import requests
from core.config import Config

class NeMoClient:
    def __init__(self):
        self.api_key = Config.NVIDIA_API_KEY
        self.endpoint = "https://api.nvidia.com/v1/llm"  # Example placeholder

    def generate(self, prompt):
        if not self.api_key:
            raise ValueError("NVIDIA API key not found")

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "prompt": prompt,
            "max_tokens": 512
        }

        response = requests.post(self.endpoint, json=payload, headers=headers)

        return response.json()