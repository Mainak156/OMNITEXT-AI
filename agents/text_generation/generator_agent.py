class GeneratorAgent:
    def __init__(self):
        self.model = None

    def run(self, prompt):
        if self.model is None:
            from .model import load_model
            self.model = load_model()

        result = self.model(
            prompt,
            max_new_tokens=400,
            do_sample=True,
            temperature=0.75,
            truncation=True,
            num_return_sequences=1
        )

        return result[0]["generated_text"]