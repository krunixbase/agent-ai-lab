import os
from openai import AsyncOpenAI

class OpenAIClientFactory:
    _client = None

    @staticmethod
    def get_client():
        if OpenAIClientFactory._client is None:
            OpenAIClientFactory._client = AsyncOpenAI(
                api_key=os.getenv("OPENAI_API_KEY")
            )
        return OpenAIClientFactory._client
