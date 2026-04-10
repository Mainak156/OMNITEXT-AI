from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import re

model = SentenceTransformer("all-MiniLM-L6-v2")

def clean_text(text):
    # Remove HTML tags like <br>, <div>, etc.
    text = re.sub(r"<.*?>", " ", text)

    # Replace arrows, bullets with newline
    text = re.sub(r"[•●▪►→]", "\n- ", text)

    # Fix hyphen spacing
    text = re.sub(r"\s*-\s*", " - ", text)

    # Remove weird multiple symbols
    text = re.sub(r"[^\w\s.,:;()\-\n]", " ", text)

    # Normalize newlines
    text = re.sub(r"\n+", "\n", text)

    # Normalize spaces
    text = re.sub(r"[ \t]+", " ", text)

    return text.strip()

def process_pdf_query(pdf_file, question):
    reader = PdfReader(pdf_file)
    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"

    text = clean_text(text)

    chunks = split_text(text)

    embeddings = model.encode(chunks)
    index = faiss.IndexFlatL2(len(embeddings[0]))
    index.add(np.array(embeddings))

    q_embed = model.encode([question])
    _, indices = index.search(np.array(q_embed), k=3)

    context = "\n\n".join([chunks[i] for i in indices[0]])

    from llm.nim_client import NIMClient
    llm = NIMClient()

    prompt = f"""
Answer the question using the context below.

⚠️ Format the answer cleanly using bullet points or paragraphs.
Do NOT include HTML tags.

Context:
{context}

Question:
{question}
"""

    return llm.generate(prompt)


def split_text(text, chunk_size=500):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i+chunk_size]))

    return chunks