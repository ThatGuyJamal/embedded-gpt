import urllib.parse

from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.llms.ollama import Ollama
from langchain.prompts import PromptTemplate

from .database import Database

class LLM():
    """
    This class manages the LLM (large Language Model) and its operations.
    """

    def __init__(self):
        self.ollama = Ollama(base_url='http://localhost:11434', model="thatguyjamal/codellama")
        self.db = Database()

    def ingest_web_documents(self, url: str, chunk_size: int = 400, chunk_overlap: int = 10):
        """
        Here we documents from the web and convert them into embeddings.

        url: The URL to ingest documents from.
        """
        if url is None:
            print("No URL provided! Try again.")
            return

        parsed_url = urllib.parse.urlparse(url)
        if parsed_url.scheme not in ["http", "https"]:
            print("Invalid URL, try again.")
            return

        loader = WebBaseLoader(url)
        data = loader.load()
        print("Loaded %d documents" % len(data))

        text_splitter=RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        all_splits = text_splitter.split_documents(data)

        print("Split into %d chunks" % len(all_splits))

        self.db.add_embeds(docs=all_splits)
        
        print("Added %d documents to database" % len(all_splits))
        print("There are", self.db.total_documents(), "documents in the database")

    def prompt(self):
        """
        Prompt the user for a question and generate an answer.
        """
        question = input("Enter a prompt: ")

        # Check if question is empty
        if question == "":
            print("Question cannot be empty, try again.")
            return
        
        # Generate answer
        if self.db.vectorStore is None:
            print("You need to ingest documents first before prompting.")
            return
        
        prompt_template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.

        {context}

        Question: {question}
        """
        PROMPT = PromptTemplate(
            template=prompt_template, input_variables=["context", "question"]
        )
        
        try:
            qa = RetrievalQA.from_chain_type(self.ollama, chain_type="stuff", retriever=self.db.vectorStore.as_retriever(), chain_type_kwargs={"prompt": PROMPT},)
            docs = qa({"query": question})

            print(docs['result'])
        except Exception as e:
            print("Error:", e)
            print("[NOTE]: This error is probably coming from the vectorStore being None, this will be fixed soon, but for now you have to run the ingest command to fix this :/")
            return