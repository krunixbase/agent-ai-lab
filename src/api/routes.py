from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from agent_core.base_agent import BaseAgent
from pipelines.llm_pipeline import OpenAILLMPipeline
from pipelines.retrieval_pipeline import SimpleRetrievalPipeline

router = APIRouter()

class RunRequest(BaseModel):
    prompt: str

@router.post("/agent/run")
async def run_agent(req: RunRequest):
    try:
        agent = BaseAgent(
            llm=OpenAILLMPipeline(client=None, model="gpt-4o-mini"),
            retriever=SimpleRetrievalPipeline(["example doc 1"])
        )
        return await agent.run(req.prompt)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
