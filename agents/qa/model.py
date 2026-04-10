from transformers import pipeline
from core.config import Config

def load_model():
    return pipeline(
        "question-answering",
        model=Config.QA_MODEL
    )