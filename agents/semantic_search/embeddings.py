from sentence_transformers import SentenceTransformer
from core.config import Config

def load_embedding_model():
    return SentenceTransformer(Config.EMBEDDING_MODEL)