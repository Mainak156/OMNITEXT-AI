class NERAgent:
    def __init__(self):
        self.model = None

    def run(self, text):
        if self.model is None:
            from .model import load_model
            self.model = load_model()

        entities = self.model(text)

        formatted = []
        for ent in entities:
            formatted.append({
                "entity": ent["entity_group"],
                "word": ent["word"],
                "score": round(ent["score"], 3)
            })

        return formatted