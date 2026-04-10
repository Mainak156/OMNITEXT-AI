from llm.llm_router import llm_router


def aggregate_results(results, tasks=None, user_input=None):
    """
    Aggregates outputs from multiple NLP agents.
    Uses LLM for intelligent response generation.
    Falls back to rule-based formatting if LLM fails.
    """

    # =========================
    # 🔥 Primary: LLM Processing
    # =========================
    try:
        return llm_router.process(tasks, results, user_input)

    except Exception as e:
        print("⚠️ LLM failed, using fallback:", str(e))

    # =========================
    # ⚙️ Fallback Formatting
    # =========================
    output = "\n===== NLP-OS OUTPUT =====\n"

    # 📝 Summary
    if "summary" in results:
        output += f"\n📝 SUMMARY:\n{results['summary']}\n"

    # 💬 Sentiment
    if "sentiment" in results:
        sentiment = results["sentiment"][0]
        output += f"\n💬 SENTIMENT:\n{sentiment['label']} (confidence: {round(sentiment['score'], 3)})\n"

    # 🏷️ Named Entities
    if "entities" in results:
        output += "\n🏷️ ENTITIES:\n"
        for ent in results["entities"]:
            output += f"- {ent['word']} ({ent['entity']})\n"

    # 🌍 Translation
    if "translation" in results:
        output += f"\n🌍 TRANSLATION:\n{results['translation']}\n"

    # ❓ QA
    if "answer" in results:
        output += f"\n❓ ANSWER:\n{results['answer']}\n"

    # ✍️ Generated Text
    if "generated_text" in results:
        output += f"\n✍️ GENERATED TEXT:\n{results['generated_text']}\n"

    # 🔍 Semantic Search
    if "search" in results:
        output += "\n🔍 SEARCH RESULTS:\n"
        for item in results["search"]:
            output += f"- {item}\n"

    return output