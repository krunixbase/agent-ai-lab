from typing import List, Dict
from utils.validators import ensure_not_empty
from utils.timing import measure_time
from utils.json_safe import json_safe


class RetrievalPipeline:
    """
    Abstract retrieval interface.
    """

    async def search(self, query: str, top_k: int = 3) -> List[Dict]:
        raise NotImplementedError


class SimpleRetrievalPipeline(RetrievalPipeline):
    """
    Dummy in-memory retrieval for testing.
    """

    def __init__(self, documents: List[str]):
        self.documents = documents

    @measure_time
    async def search(self, query: str, top_k: int = 3) -> List[Dict]:
        ensure_not_empty(query)

        results = [
            {"text": doc, "score": 1.0}
            for doc in self.documents
            if query.lower() in doc.lower()
        ]

        return results[:top_k]
