import time 
import logfire
from langchain_google_genai import GoogleGenerativeAIEmbeddings


BATCH_SIZE = 50
_GEMINI_DIM = 3072
_FALLBACK_DIM = 768

_active_model = None
_model_type : str | None = None


def _probe_gimini():
    ''' Try on embed call to verify gimini is rechable or not . Return model or None'''

def _load_fallback():
    return

def _init():
    return

def get_embedding_dim() -> int :
    """ return the vector dimension of active embedding model after . call after init()"""
    return

def _embed_batch(batch :list[str]) -> list[list[float]]:
    return 

def _embed_querry(querry:str) -> list[float]:
    return

def _embed_texts(texts : list[str] ) -> list[list[float]] :
    _init()
