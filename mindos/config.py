import os
import logging
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("MINDOS")

class Config:
    @staticmethod
    def validate():
        if not GROQ_API_KEY:
            raise ValueError("A variável de ambiente GROQ_API_KEY é obrigatória no arquivo .env")

Config.validate()