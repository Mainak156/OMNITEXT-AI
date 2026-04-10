from transformers import pipeline
from core.config import Config

def load_model():
    return pipeline(
        "translation",
        model=Config.TRANSLATION_MODEL
    )