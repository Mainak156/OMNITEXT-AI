class QAAgent:
    def __init__(self):
        self.model = None

    def run(self, question, context):
        if self.model is None:
            from .model import load_model
            self.model = load_model()

        return self.model(
            question=question,
            context=context
        )