import numpy as np
from .embeddings import load_embedding_model
from .vector_store import VectorStore

class SemanticSearchAgent:
    def __init__(self):
        self.model = None
        self.store = None
        self.initialized = False

    def _initialize(self):
        if not self.initialized:
            self.model = load_embedding_model()
            self.store = VectorStore()

            docs = [
                "AI is transforming industries",
                "Machine learning enables prediction",
                "Deep learning uses neural networks"
            ]

            embeddings = self.model.encode(docs)
            self.store.add(embeddings, docs)

            self.initialized = True

    def search(self, query, k=3):
        self._initialize()

        q_emb = self.model.encode([query])
        return self.store.search(np.array(q_emb), k)