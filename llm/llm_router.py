from llm.nim_client import NIMClient
from llm.prompt_templates import build_prompt

class LLMRouter:
    def __init__(self):
        # 🔥 Primary + fallback models
        self.primary = NIMClient("openai/gpt-oss-20b")
        self.fallback = NIMClient("meta/llama3-8b-instruct")

    def process(self, tasks, results, user_input):
        prompt = build_prompt(tasks, results, user_input)

        try:
            return self.primary.generate(prompt)

        except Exception as e:
            print("⚠️ Primary model failed, switching to fallback...")
            return self.fallback.generate(prompt)


# singleton
llm_router = LLMRouter()