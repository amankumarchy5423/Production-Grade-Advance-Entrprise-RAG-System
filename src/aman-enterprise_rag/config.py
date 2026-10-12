import os
from dotenv import load_dotenv
from dataclasses import dataclass


load_dotenv()

@dataclass(frozen=True)
class setting:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GROQ_FALLBACK_API_KEY = os.getenv("GROQ_FALLBACK_API_KEY")
    GROQ_MODEL = "llama-3.3-70b-versatile"

    QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
    QUDRANT_CLUSTER_ENDPOINT = os.getenv("QUDRANT_CLUSTER_ENDPOINT")
    QUDRANT_COLLECTION = "Enterprise_aman_RAG"

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")




