from transformers import pipeline
from core.config import Config

def load_model():
    return pipeline(
        "summarization",
        model=Config.SUMMARIZATION_MODEL
    )