from .model import load_model

class SentimentAgent:
    def __init__(self):
        self.model = None

    def run(self, text):
        if self.model is None:
            self.model = load_model()

        return self.model(text)