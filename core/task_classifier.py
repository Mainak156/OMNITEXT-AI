def classify_task(text):
    text = text.lower()
    tasks = []

    if "summarize" in text or "summary" in text:
        tasks.append("summarization")

    if "translate" in text:
        tasks.append("translation")

    if "sentiment" in text or "feeling" in text:
        tasks.append("sentiment")

    if "entity" in text or "name" in text:
        tasks.append("ner")

    if "question" in text or "answer" in text:
        tasks.append("qa")

    if "search" in text or "find" in text:
        tasks.append("semantic_search")

    # 🔥 NEW: better generation detection
    if any(word in text for word in ["generate", "write", "create", "joke", "story"]):
        tasks.append("generation")

    return tasks