from typing import Any, Optional, List

import chromadb
from langchain.llms.ollama import Ollama
from langchain.vectorstores.chroma import Chroma
from langchain.embeddings import OllamaEmbeddings

class Database:
    """
    Database class for storing embeddings and querying them
    """

    def __init__(self, ollama: Ollama) -> None:
        client = chromadb.PersistentClient("./db/convex")
        self._collection_name = "convex-docs"
        self.ollama_embed_func = OllamaEmbeddings(base_url='http://localhost:11434', model="codellama:7b")

        self.langchain_chroma = Chroma(
            client=client,
            embedding_function=self.ollama_embed_func,
            collection_name="convex-docs",
        )

        self.vectorStore = Chroma | None

    def add_embeds(self, docs: List[chromadb.Documents], meta: Optional[Any] = None):
        """
        Add embeddings to the database
        """
        print("Adding %d documents to database and collection %s" % (len(docs), self._collection_name))
        vectorstore = self.langchain_chroma.from_documents(collection_name=self._collection_name, documents=docs, embedding=self.ollama_embed_func, collection_metadata=meta)
        print("Done adding documents to database")

        self.vectorStore = vectorstore
