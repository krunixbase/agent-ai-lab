import httpx

class OllamaClient:
    def __init__(self, model: str = "llama3.2"):
        self.model = model

    async def generate(self, prompt: str):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False
                }
            )
            data = response.json()
            return {
                "text": data.get("response", "")
            }
