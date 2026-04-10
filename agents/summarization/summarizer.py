class SummarizerAgent:
    def __init__(self):
        self.model = None

    def run(self, text):
        if self.model is None:
            from .model import load_model
            self.model = load_model()

        words = text.split()

        if len(words) < 20:
            return text

        max_len = int(len(words) * 0.6)
        min_len = int(len(words) * 0.3)

        result = self.model(
            text,
            max_length=max_len,
            min_length=min_len,
            do_sample=False
        )

        return result[0]["summary_text"]