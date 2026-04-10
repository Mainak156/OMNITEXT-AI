from transformers import pipeline
from core.config import Config

def load_model():
    return pipeline(
        "text-generation",
        model=Config.GENERATION_MODEL
    )