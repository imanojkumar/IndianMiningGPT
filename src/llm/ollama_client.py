"""
IndianMiningGPT
Ollama Client
"""

import requests


OLLAMA_URL = "http://127.0.0.1:11434/api/generate"

MODEL_NAME = "gemma3:4b"


class OllamaClient:

    def __init__(
        self,
        model_name=MODEL_NAME,
        timeout=300
    ):

        self.model_name = model_name
        self.timeout = timeout

    def generate(
        self,
        prompt,
        temperature=0.1
    ):

        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": temperature
            }
        }

        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=self.timeout
        )

        response.raise_for_status()

        data = response.json()

        return data.get(
            "response",
            ""
        ).strip()
