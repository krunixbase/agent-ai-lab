from fastapi import FastAPI
from pydantic import BaseModel

from src.agent_core.base_agent import BaseAgent
from src.agent_core.memory import Memory
from src.agent_core.tools import ToolRegistry
from src.pipelines.llm_pipeline import LLMPipeline

app = FastAPI(title="Agent AI Lab")

class AgentRequest(BaseModel):
    prompt: str

@app.post("/agent/run")
async def run_agent(request: AgentRequest):
    llm = LLMPipeline()
    memory = Memory()
    tools = ToolRegistry()

    agent = BaseAgent(llm=llm, memory=memory, tools=tools)
    result = agent.run(request.prompt)

    return {"response": result}

@app.get("/health")
async def health():
    return {"status": "ok"}
