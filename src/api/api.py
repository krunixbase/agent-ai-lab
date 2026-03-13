from fastapi import FastAPI
from pydantic import BaseModel

from src.agent.base_agent import BaseAgent
from src.memory.memory import Memory
from src.tools.tools import ToolRegistry
from src.pipelines.openai_pipeline import OpenAIPipeline

app = FastAPI(title="Agent AI Lab")


class AgentRequest(BaseModel):
    prompt: str


@app.post("/agent/run")
async def run_agent(request: AgentRequest):
    pipeline = OpenAIPipeline()
    memory = Memory()
    tools = ToolRegistry()

    agent = BaseAgent(pipeline=pipeline, tools=tools, memory=memory)
    result = agent.run(request.prompt)

    return {"response": result}


@app.get("/health")
async def health():
    return {"status": "ok"}
