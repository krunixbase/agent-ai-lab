from typing import Optional, Dict, Any

from pipelines.llm_pipeline import LLMPipeline
from pipelines.retrieval_pipeline import RetrievalPipeline

from .memory import Memory
from .reasoning import ReasoningEngine
from .tools import ToolRegistry

# --- utils ---
from utils.uuid import short_uuid
from utils.timing import measure_time
from utils.validators import ensure_not_empty
from utils.formatting import truncate, pretty_json


class BaseAgent:
    """
    Core agent class orchestrating:
    - reasoning loop
    - memory
    - retrieval
    - tool execution
    - LLM calls
    """

    def __init__(
        self,
        llm: LLMPipeline,
        retriever: Optional[RetrievalPipeline] = None,
    ):
        self.llm = llm
        self.retriever = retriever
        self.memory = Memory()
        self.reasoning = ReasoningEngine()
        self.tools = ToolRegistry()

        # Unique session identifier
        self.session_id = short_uuid()

    # -------------------------------------------------------------------------
    # MAIN ENTRY POINT
    # -------------------------------------------------------------------------

    @measure_time
    async def run(self, prompt: str) -> Dict[str, Any]:
        """
        Main agent execution loop.
        """

        # Validate input
        ensure_not_empty(prompt, name="prompt")

        # 1. Retrieve context (RAG)
        context = ""
        if self.retriever:
            results = await self.retriever.search(prompt, top_k=3)
            context = "\n".join([r["text"] for r in results])

        # 2. Build system prompt
        system_prompt = self.reasoning.build_system_prompt(context=context)

        # 3. Generate LLM response
        response = await self.llm.generate(
            prompt=f"{system_prompt}\nUser: {prompt}"
        )

        # 4. Store memory
        self.memory.add_interaction(prompt, response["text"])

        # 5. Return final output (clean + readable)
        return {
            "session_id": self.session_id,
            "response": response["text"],
            "context_used": truncate(context, 500),
            "raw": pretty_json(response["raw"]),
        }
