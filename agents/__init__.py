

from .DeepSeekR1 import DeepSeekAgent
from .Graphiti import GraphitiAgent
from dotenv import load_dotenv

load_dotenv()

MAIN_AGENT = DeepSeekAgent()
KG_AGENT = GraphitiAgent()