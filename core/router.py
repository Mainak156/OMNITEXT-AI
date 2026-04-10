from agents.summarization.summarizer import SummarizerAgent
from agents.sentiment.sentiment_agent import SentimentAgent
from agents.ner.ner_agent import NERAgent
from agents.qa.qa_agent import QAAgent
from agents.translation.translator import TranslatorAgent
from agents.semantic_search.search_agent import SemanticSearchAgent
from agents.text_generation.generator_agent import GeneratorAgent

# Initialize agents once (important for performance)
summarizer = SummarizerAgent()
sentiment = SentimentAgent()
ner = NERAgent()
qa = QAAgent()
translator = TranslatorAgent()
search = SemanticSearchAgent()
generator = GeneratorAgent()

def extract_text(user_input):
    if ":" in user_input:
        return user_input.split(":", 1)[1].strip()
    return user_input

def route_tasks(tasks, user_input, context=None):
    results = {}

    for task in tasks:
        print(f"→ Running {task} agent")

        if task == "summarization":
            clean_text = extract_text(user_input)
            results["summary"] = summarizer.run(clean_text)

        elif task == "sentiment":
            clean_text = extract_text(user_input)
            results["sentiment"] = sentiment.run(clean_text)

        elif task == "ner":
            results["entities"] = ner.run(user_input)

        elif task == "qa":
            if context:
                results["answer"] = qa.run(user_input, context)
            else:
                results["answer"] = "No context provided"

        elif task == "translation":
            results["translation"] = translator.run(user_input)

        elif task == "semantic_search":
            results["search"] = search.search(user_input)

        elif task == "generation":
            results["generated_text"] = generator.run(user_input)

    return results