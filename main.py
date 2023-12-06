import time

from lib.cli import CLI

def main():
    cli = CLI()

    while True:
        command = input("Enter a command or type 'help': ")
        cli.run_command(command)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))