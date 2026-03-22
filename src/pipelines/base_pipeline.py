from abc import ABC, abstractmethod
from utils.timing import measure_time
from utils.validators import ensure_not_empty


class BasePipeline(ABC):
    """
    Base class for all pipelines (LLM, retrieval, etc.)
    """

    @abstractmethod
    @measure_time
    async def run(self, *args, **kwargs):
        pass

    def validate(self, text: str, name: str = "input"):
        ensure_not_empty(text, name)
