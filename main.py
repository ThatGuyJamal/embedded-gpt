import time

from lib.cli import CLI

def main():
    cli = CLI()

    while True:
        command = input("Enter a command or type 'help' to view the commands: ")
        cli.run_command(command)


if __name__ == "__main__":
    main()