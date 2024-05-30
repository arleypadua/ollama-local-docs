import os

from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import Ollama
from langchain.chains import RetrievalQA

from settings import Settings

class Model:
    def __init__(self, settings: Settings):
        """
        Initialize the model
        
        Warning: this will use Ollama and Chroma to load up everything in memory, so it might take a while and is quite memory intensive
        """
        self.settings = settings
        self.embeddings = HuggingFaceEmbeddings(model_name=settings.embeddings_model_name)
        self.db = Chroma(persist_directory=settings.persist_directory, embedding_function=self.embeddings)
        self.retriever = self.db.as_retriever(search_kwargs={"k": settings.target_source_chunks})
        self.llm = Ollama(model=settings.model)
        self.qa = RetrievalQA.from_chain_type(llm=self.llm, chain_type="stuff", retriever=self.retriever, return_source_documents= not settings.hide_source)
    
    def ask(self, query):
        """
        Process a query and return the answer along with source documents if not hidden.

        Args:
            query (str): The query string to be processed.

        Returns:
            tuple: A tuple containing:
                - answer (str): The generated answer from the model.
                - docs (list): A list of source documents if the environment variable `HIDE_SOURCE_FILES` is False, otherwise an empty list.
        
        Example:
            answer, docs = model_instance.ask("What is the capital of France?")
        """
        res = self.qa(query)
        answer = res['result']
        docs = []
        
        if not self.settings.hide_source:
            for doc in res['source_documents']:
                doc_info = {
                    "file_path": doc.metadata["file_path"],
                    "page": doc.metadata["page"],
                    "text": doc.page_content,
                    "source": doc.metadata["source"],
                }
                docs.append(doc_info)
        
        return answer, docs