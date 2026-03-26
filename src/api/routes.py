from fastapi import APIRouter
from pydantic import BaseModel
from pipelines.llm_pipeline import LLMPipeline
from agents.base_agent import BaseAgent
from pipelines.retrieval_pipeline import SimpleRetrievalPipeline
from fastapi.responses import StreamingResponse
from typing import AsyncGenerator
import json

router = APIRouter()


# Request schema
class RunRequest(BaseModel):
    prompt: str
    model: str = "llama3.2"   # default model


# Response schema
class RunResponse(BaseModel):
    text: str
    model: str

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



@router.post("/stream_sse")
async def stream_sse(req: RunRequest):
    """
    SSE streaming endpoint for real-time token generation.
    Compatible with EventSource in frontend.
    """

    llm = LLMPipeline(model=req.model)

    async def event_generator() -> AsyncGenerator[str, None]:
        async for chunk in llm.stream(req.prompt):
            # Format as SSE event
            data = json.dumps({"token": chunk})
            yield f"data: {data}\n\n"

        # Signal completion
        yield "data: [DONE]\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream"
    )
