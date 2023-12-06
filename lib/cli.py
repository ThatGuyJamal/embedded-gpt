
from lib.llm import LLM

class CLI():
    def __init__(self):
        self.llm = LLM()
        self.commands = {
            "help": (self.help, "Display this help message"),
            "ingest": (self.ingest, "Ingest documents from the web"),
            "prompt": (self.prompt, "Prompt the user for a question and generate an answer"),
            "delete": (self.delete, "Delete a collection from the database."),
            "stats": (self.stats, "Stats about the LLM and database"),
            "exit": (self.exit, "Exit the program"),
        }

    def run_command(self, command: str):
        """
        Run a command
        """
        if command in self.commands:
            self.commands[command][0]()
        else:
            print("Command not found, try again.")

    def help(self):
        """
        Print help message
        """
        print("Available commands:")
        for command, (_, description) in self.commands.items():
            print(f"{command}: {description}")

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

    def delete(self):
        """
        Delete a collection from the database
        """
        print("Available collections to delete: %s" % self.llm.db.get_collection_names())
        collection_name = input("Enter the name of the collection to delete: ")
        self.llm.db.delete_collection(collection_name=collection_name)

    def stats(self):
        """
        Stats about the LLM and database
        """
        print("Stats:")
        print("Running LLM type: ollama, model: thatguyjamal/codellama, version: 0.1.12")
        print("Current Documentations: %s" % self.llm.db.total_documents())

    def exit(self):
        """
        Exit the program
        """
        exit()