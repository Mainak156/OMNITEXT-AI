from transformers import pipeline
from core.config import Config

def load_model():
    return pipeline(
        "ner",
        model=Config.NER_MODEL,
        aggregation_strategy="simple"
    )