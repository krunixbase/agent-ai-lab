from fastapi import APIRouter
from pydantic import BaseModel
from pipelines.llm_pipeline import LLMPipeline
from agents.base_agent import BaseAgent
from pipelines.retrieval_pipeline import SimpleRetrievalPipeline
from fastapi.responses import StreamingResponse
from typing import AsyncGenerator

router = APIRouter()


# Request schema
class RunRequest(BaseModel):
    prompt: str
    model: str = "llama3.2"   # default model


# Response schema
class RunResponse(BaseModel):
    text: str
    model: str


@router.post("/run", response_model=RunResponse)
async def run_agent(req: RunRequest):
    """
    Main endpoint for generating responses using local Ollama models.
    """

    # Initialize LLM pipeline with selected model
    llm = LLMPipeline(model=req.model)

    # Simple retrieval (you can replace this later)
    retriever = SimpleRetrievalPipeline(["example document"])

    # Create agent
    agent = BaseAgent(
        llm=llm,
        retriever=retriever
    )

    # Run agent
    result = await agent.run(req.prompt)

    return RunResponse(
        text=result["text"],
        model=req.model
    )

@router.post("/stream")
async def stream_response(req: RunRequest):
    """
    Streaming endpoint for real-time token generation.
    """

    llm = LLMPipeline(model=req.model)

    async def event_generator() -> AsyncGenerator[str, None]:
        async for chunk in llm.stream(req.prompt):
            yield chunk + "\n"

    return StreamingResponse(event_generator(), media_type="text/plain")
