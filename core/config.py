import os
from dotenv import load_dotenv

# =========================
# Load Environment Variables
# =========================
load_dotenv()


class Config:
    # =========================
    # General Settings
    # =========================
    DEBUG = os.getenv("DEBUG", "True") == "True"
    APP_NAME = "NLP-OS"
    ENV = os.getenv("ENV", "development")

    # =========================
    # Model Settings (Local HF)
    # =========================
    SUMMARIZATION_MODEL = "sshleifer/distilbart-cnn-12-6"
    TRANSLATION_MODEL = "Helsinki-NLP/opus-mt-en-fr"
    QA_MODEL = "distilbert-base-cased-distilled-squad"
    SENTIMENT_MODEL = "distilbert-base-uncased-finetuned-sst-2-english"
    NER_MODEL = "dbmdz/bert-large-cased-finetuned-conll03-english"

    # ⚠️ GPT-2 kept only as fallback (not recommended)
    GENERATION_MODEL = "gpt2"

    # =========================
    # NVIDIA LLM Settings 🔥
    # =========================
    NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")
    NVIDIA_BASE_URL = os.getenv("NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1")

    # Model routing
    NVIDIA_FAST_MODEL = "gpt-oss-20b"
    NVIDIA_SMART_MODEL = "gpt-oss-120b"

    # Whisper (voice)
    NVIDIA_WHISPER_MODEL = "whisper-large-v3"

    # =========================
    # Embeddings / Search
    # =========================
    EMBEDDING_MODEL = "all-MiniLM-L6-v2"
    VECTOR_DB_TYPE = os.getenv("VECTOR_DB_TYPE", "faiss")  # "faiss" or "chroma"

    # =========================
    # RAG Settings
    # =========================
    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 500))
    CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 50))
    TOP_K_RESULTS = int(os.getenv("TOP_K_RESULTS", 3))

    # =========================
    # Input / Output Limits
    # =========================
    MAX_INPUT_LENGTH = int(os.getenv("MAX_INPUT_LENGTH", 1024))
    MAX_OUTPUT_LENGTH = int(os.getenv("MAX_OUTPUT_LENGTH", 256))

    # =========================
    # Paths
    # =========================
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    DATA_DIR = os.path.join(BASE_DIR, "data")
    RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
    PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")
    EMBEDDINGS_DIR = os.path.join(DATA_DIR, "embeddings")

    LOG_DIR = os.path.join(BASE_DIR, "logs")

    # =========================
    # Logging
    # =========================
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    # =========================
    # Performance / Runtime
    # =========================
    DEVICE = "cuda" if os.getenv("USE_CUDA", "False") == "True" else "cpu"
    BATCH_SIZE = int(os.getenv("BATCH_SIZE", 8))

    # =========================
    # Safety / Fallbacks
    # =========================
    ENABLE_LLM = os.getenv("ENABLE_LLM", "True") == "True"
    FALLBACK_TO_LOCAL = True  # if NVIDIA fails

    # =========================
    # Validation (IMPORTANT)
    # =========================
    @staticmethod
    def validate():
        if Config.ENABLE_LLM and not Config.NVIDIA_API_KEY:
            print("⚠️ Warning: NVIDIA API key not set. Falling back to local models.")