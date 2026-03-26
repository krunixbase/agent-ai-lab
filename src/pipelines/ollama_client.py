from fastapi import APIRouter
from pydantic import BaseModel
from pipelines.llm_pipeline import LLMPipeline
from agents.base_agent import BaseAgent
from pipelines.retrieval_pipeline import SimpleRetrievalPipeline

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
