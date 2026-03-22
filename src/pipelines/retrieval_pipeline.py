import os
from typing import List, Dict, Any, Optional

import chromadb
from chromadb.config import Settings as ChromaSettings

import numpy as np
import httpx


class RetrievalPipeline:
    """
    Unified retrieval pipeline supporting:
    - Chroma (local vector DB)
    - Postgres pgvector (future)
    - Pinecone (future)
    - Custom embedding models

    Provides:
    - embedding generation
    - vector search
    - document retrieval
    - metadata filtering
    """

    def __init__(
        self,
        provider: str = "chroma",
        collection: str = "documents",
        embedding_model: str = "text-embedding-3-small",
    ):
        self.provider = provider.lower()
        self.collection_name = collection
        self.embedding_model = embedding_model

        # Embedding API key (OpenAI)
        self.openai_key = os.getenv("OPENAI_API_KEY")

        # Initialize vector DB
        if self.provider == "chroma":
            self._init_chroma()

        else:
            raise ValueError(f"Unsupported retrieval provider: {self.provider}")

    # -------------------------------------------------------------------------
    # INITIALIZATION
    # -------------------------------------------------------------------------

    def _init_chroma(self):
        db_path = os.getenv("VECTOR_DB_PATH", "./vector_store")

        self.chroma_client = chromadb.Client(
            ChromaSettings(
                chroma_db_impl="duckdb+parquet",
                persist_directory=db_path,
            )
        )

        self.collection = self.chroma_client.get_or_create_collection(
            name=self.collection_name,
            metadata={"hnsw:space": "cosine"},
        )

    # -------------------------------------------------------------------------
    # EMBEDDINGS
    # -------------------------------------------------------------------------

    async def embed(self, text: str) -> List[float]:
        """
        Generate embeddings using OpenAI embedding models.
        """

        if not self.openai_key:
            raise RuntimeError("Missing OPENAI_API_KEY for embeddings")

        url = "https://api.openai.com/v1/embeddings"

        headers = {
            "Authorization": f"Bearer {self.openai_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": self.embedding_model,
            "input": text,
        }

        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(url, json=payload, headers=headers)
            response.raise_for_status()
            data = response.json()

        return data["data"][0]["embedding"]

    # -------------------------------------------------------------------------
    # ADD DOCUMENTS
    # -------------------------------------------------------------------------

    async def add_documents(
        self,
        documents: List[str],
        metadatas: Optional[List[Dict[str, Any]]] = None,
        ids: Optional[List[str]] = None,
    ):
        """
        Add documents to the vector store.
        """

        embeddings = []
        for doc in documents:
            emb = await self.embed(doc)
            embeddings.append(emb)

        self.collection.add(
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids,
        )

    # -------------------------------------------------------------------------
    # SEARCH
    # -------------------------------------------------------------------------

    async def search(
        self,
        query: str,
        top_k: int = 5,
        where: Optional[Dict[str, Any]] = None,
    ) -> List[Dict[str, Any]]:
        """
        Perform vector search using embeddings + Chroma.
        """

        query_embedding = await self.embed(query)

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            where=where,
        )

        output = []
        for i in range(len(results["documents"][0])):
            output.append(
                {
                    "text": results["documents"][0][i],
                    "score": results["distances"][0][i],
                    "metadata": results["metadatas"][0][i],
                }
            )

        return output
