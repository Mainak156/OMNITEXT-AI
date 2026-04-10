class TranslatorAgent:
    def __init__(self):
        self.model = None

    def run(self, text):
        if self.model is None:
            from .model import load_model
            self.model = load_model()

        result = self.model(text)
        return result[0]["translation_text"]