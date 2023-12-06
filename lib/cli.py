
from lib.database import Database
from lib.llm import LLM
from langchain.llms.ollama import Ollama

class CLI():
    def __init__(self):
        self.llm = LLM()
        self.commands = {
            "help": self.help,
            "ingest": self.ingest,
            "prompt": self.prompt,
            "exit": self.exit
        }

    def run_command(self, command: str):
        """
        Run a command
        """
        if command in self.commands:
            self.commands[command]()
        else:
            print("Command not found, try again.")

    def help(self):
        """
        Print help message
        """
        print("Available commands:")
        for command in self.commands:
            print(command)

    def ingest(self):
        """
        Ingest documents from the web
        """
        custom_url = input("Enter a URL to ingest documents from (leave blank for default): ")
        if custom_url == "":
            custom_url = None
        self.llm.ingest_web_documents(url=custom_url)

    def prompt(self):
        """
        Prompt the user for a question and generate an answer.
        """
        self.llm.prompt()

    def exit(self):
        """
        Exit the program
        """
        exit()