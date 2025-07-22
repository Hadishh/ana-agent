import os
import json
import asyncio
from datetime import datetime

from graphiti_core import Graphiti
from graphiti_core.llm_client.config import LLMConfig
from graphiti_core.llm_client.openai_client import OpenAIClient
from graphiti_core.embedder.openai import OpenAIEmbedder, OpenAIEmbedderConfig
from graphiti_core.nodes import EpisodeType
from graphiti_core.utils.bulk_utils import RawEpisode
from tqdm import tqdm

class GraphitiAgent:
    async def initialize_database(self):
        await self.graphiti.build_indices_and_constraints()
        with open("kg/initial_docs.txt", "r") as f:
                for i, line in enumerate(tqdm(f.readlines())): 
                    try:
                        await self.graphiti.add_episode(
                            name=f"import:data:{i}",
                            episode_body=line.strip(),
                            source=EpisodeType.text,
                            source_description="docstring data",
                            reference_time=datetime.now(),
                        )
                    except:
                        print(f"Ignoring doc : {line}")
                    

        # await self.graphiti.add_episode_bulk(episodes)

        result = await self.graphiti.search("who is the son of arthur morgan?")
        # res2 = await self.graphiti.search("arthur morgan phone number?")

        pass


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

        
        # asyncio.run(self.initilaze_triplets())

        # res = asyncio.run(self.graphiti.search("who is the son of arthur morgan?"))
        pass

        