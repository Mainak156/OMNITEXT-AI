def build_prompt(tasks, results, user_input):
    return f"""
You are an intelligent NLP system.

User Query:
{user_input}

We performed the following NLP tasks:
{tasks}

Here are the results:

Summary:
{results.get("summary", "")}

Sentiment:
{results.get("sentiment", "")}

Entities:
{results.get("entities", "")}

Translation:
{results.get("translation", "")}

Answer:
{results.get("answer", "")}

Generated Text:
{results.get("generated_text", "")}

Task:
- Combine all outputs into a clean, human-readable response
- Be concise and clear
- Explain if necessary
"""