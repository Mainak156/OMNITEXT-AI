from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class NIMClient:
    def __init__(self, model_name="openai/gpt-oss-20b"):
        self.model_name = model_name

        self.client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=os.getenv("NVIDIA_API_KEY")
        )

    def generate(self, prompt):
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5,
                stream=False  # ✅ non-streaming
            )

            # ✅ Correct extraction
            return response.choices[0].message.content

        except Exception as e:
            print("❌ NVIDIA ERROR:", str(e))
            return "⚠️ LLM failed."