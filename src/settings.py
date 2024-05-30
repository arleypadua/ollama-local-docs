import os
from constants import CHROMA_SETTINGS

class Settings:
    def __init__(self):
        self.model = os.environ.get("MODEL", "llama3")
        self.embeddings_model_name = os.environ.get("EMBEDDINGS_MODEL_NAME", "all-MiniLM-L6-v2")
        self.persist_directory = os.environ.get("PERSIST_DIRECTORY", "./db")
        self.target_source_chunks = int(os.environ.get('TARGET_SOURCE_CHUNKS',4))
        self.hide_source = os.environ.get('HIDE_SOURCE_FILES', False)
        self.source_directory = os.environ.get('SOURCE_DIRECTORY', 'source_documents')
        self.chunk_size = 500
        self.chunk_overlap = 50
        
        self.CHROMA_SETTINGS = CHROMA_SETTINGS