from graphiti_core import Graphiti
from graphiti_core.llm_client.config import LLMConfig
from graphiti_core.llm_client.openai_client import OpenAIClient
from graphiti_core.embedder.openai import OpenAIEmbedder, OpenAIEmbedderConfig
import asyncio


import os

class GraphitiAgent:
    def __init__(self):
        llm_config = LLMConfig(
            api_key=os.getenv("OPENAI_API_KEY"),
            model=os.getenv("LLM_MODEL"),
            base_url=os.getenv("OPENAI_BASE_URL")
        )
        self.llm_client = OpenAIClient(config=llm_config)
        embedder_config = OpenAIEmbedderConfig(
            api_key=os.getenv("OPENAI_API_KEY"),
            embedding_model=os.getenv("EMBEDDER_MODEL"),
            base_url=os.getenv("OPENAI_BASE_URL_EMBEDDING"),
            embedding_dim=1024
        )
        self.embedder = OpenAIEmbedder(config=embedder_config)

        self.graphiti = Graphiti(
            uri=os.getenv("NEO4J_URI"),
            user=os.getenv("NEO4J_USER"),
            password=os.getenv("NEO4J_PASSWORD"),
            llm_client=self.llm_client,
            embedder=self.embedder
        )

        # asyncio.run(self.graphiti.build_indices_and_constraints())

        pass

        