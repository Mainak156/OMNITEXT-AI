# 🧠 OMNITEXT AI: Multi-Agent AI System with NVIDIA LLM + Voice + RAG

OMNITEXT AI is a modular, production-style **Multi-Agent NLP System** that combines:
- 🤖 Classical NLP (HuggingFace)
- 🧠 NVIDIA LLMs (GPT-OSS)
- 📄 RAG (Retrieval-Augmented Generation)
- 🎙️ Voice Input (Speech-to-Text)

It dynamically understands user intent and routes tasks to specialized agents.

---

## 🚀 Features

- 🧩 Multi-Agent Architecture (Summarization, Sentiment, NER, QA, etc.)
- 🧠 NVIDIA GPT-OSS integration for intelligent responses
- 📄 PDF Q&A using RAG (FAISS + embeddings)
- 🎙️ Voice input with transcription
- ⚡ Streamlit-based UI
- 🔌 Modular & scalable design

---

## 🏗️ Architecture

            ┌───────────────────────┐
            │      User Input       │
            │  (Text / Voice / PDF)│
            └─────────┬─────────────┘
                      │
                      ▼
            ┌───────────────────────┐
            │   Input Processor     │
            │ (STT, PDF Extractor)  │
            └─────────┬─────────────┘
                      │
                      ▼
            ┌───────────────────────┐
            │   Task Classifier     │
            │ (Intent Detection)    │
            └─────────┬─────────────┘
                      │
                      ▼
            ┌───────────────────────┐
            │        Router         │
            │  (Agent Selection)    │
            └─────────┬─────────────┘
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
┌────────────┐ ┌────────────┐ ┌────────────┐
│ Summarizer │ │   NER      │ │ Sentiment  │
└────────────┘ └────────────┘ └────────────┘
        ▼             ▼             ▼
     (Other Agents: QA, Translation, Search, etc.)
                      │
                      ▼
            ┌───────────────────────┐
            │      Aggregator       │
            │ (Combine Responses)   │
            └─────────┬─────────────┘
                      │
                      ▼
            ┌───────────────────────┐
            │    RAG Pipeline       │
            │ (FAISS + Embeddings)  │
            └─────────┬─────────────┘
                      │
                      ▼
            ┌───────────────────────┐
            │     NVIDIA LLM        │
            │   (GPT-OSS / NIM)     │
            └─────────┬─────────────┘
                      │
                      ▼
            ┌───────────────────────┐
            │       Output          │
            │ (Text / Voice / UI)   │
            └───────────────────────┘

---

## 📂 Project Structure

omnitext-ai
│
├── app
├── core
├── agents
├── llm
├── retrieval
├── requirements.txt
└── structure.txt

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
git clone https://github.com/your-username/OMNITEXT-AI.git
cd omnitext-ai

### 2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

### 3️⃣ Install Dependencies
pip install -r requirements.txt

### 4️⃣ Setup Environment Variables
Create a `.env` file:

NVIDIA_API_KEY=your_nvidia_api_key_here
NVIDIA_BASE_URL=your_nvidia_base_url_here

---

## ▶️ Run the Project

### 🔹 CLI Mode
python main.py

### 🔹 Streamlit UI
streamlit run app/streamlit_app.py

---

## 🧠 Supported Tasks

- ✂️ Summarization  
- 🌍 Translation  
- ❓ Question Answering  
- 🧾 Named Entity Recognition (NER)  
- 😊 Sentiment Analysis  
- 🔍 Semantic Search  
- ✍️ Text Generation  

---

## 🎙️ Voice Support

- Record audio directly in UI  
- Converts WebM → WAV  
- Transcribes speech → text  
- Runs full NLP pipeline  

---

## 📄 PDF Q&A (RAG)

- Upload PDF  
- Extract text  
- Chunk + Embed  
- Retrieve relevant context  
- Generate answer  

---

## 🔥 Tech Stack

- Python  
- Streamlit  
- HuggingFace Transformers  
- Sentence Transformers  
- FAISS  
- NVIDIA NIM API (GPT-OSS)  
- Whisper (local STT)  
- pydub + ffmpeg  

---

## ⚠️ Known Issues

- Large models may require high RAM
- Whisper (NVIDIA API) may not work → fallback to local STT
- Windows may show symlink warnings (safe to ignore)

---

## 🚀 Future Improvements

- Chat memory (context awareness)
- Streaming responses
- Deployment (Docker + Cloud)
- UI enhancements

---

## 💯 One-Line Summary

OMNITEXT AI is a multi-agent AI system that processes text, voice, and documents using classical NLP + RAG + NVIDIA LLMs to generate intelligent structured outputs.

---

## 👨‍💻 Author

Mainak Sen

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it 🚀