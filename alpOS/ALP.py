import os
import sys
import shutil
import random

def ls():
    print("\n".join(os.listdir(".")))

def pwd():
    print(os.getcwd())

def cd(dir_name):
    try:
        os.chdir(dir_name)
    except FileNotFoundError:
        print(f"Directory '{dir_name}' not found.")

def mkdir(dir_name):
    try:
        os.makedirs(dir_name)
        print(f"Directory '{dir_name}' created.")
    except FileExistsError:
        print(f"Directory '{dir_name}' already exists.")

def rmdir(dir_name):
    try:
        os.rmdir(dir_name)
        print(f"Directory '{dir_name}' removed.")
    except OSError:
        print(f"Directory '{dir_name}' is not empty or does not exist.")

def touch(file_name):
    with open(file_name, 'a'):
        os.utime(file_name, None)

def rm(file_name):
    try:
        os.remove(file_name)
        print(f"File '{file_name}' removed.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")

def cp(src, dest):
    try:
        shutil.copy(src, dest)
        print(f"Copied '{src}' to '{dest}'.")
    except FileNotFoundError:
        print(f"File '{src}' not found.")

def mv(src, dest):
    try:
        shutil.move(src, dest)
        print(f"Moved '{src}' to '{dest}'.")
    except FileNotFoundError:
        print(f"File '{src}' not found.")

def help_cmd():
    commands = {
        'ls': 'List files and directories in current directory.',
        'pwd': 'Show current working directory.',
        'cd <dir>': 'Change the current directory.',
        'mkdir <dir>': 'Create a new directory.',
        'rmdir <dir>': 'Remove an empty directory.',
        'touch <file>': 'Create an empty file.',
        'rm <file>': 'Remove a file.',
        'cp <src> <dest>': 'Copy a file from src to dest.',
        'mv <src> <dest>': 'Move or rename a file.',
        'help': 'Show this help message.',
        'clear': 'Clear the terminal screen.',
        'exit': 'Exit the CLI.',
        'search <pattern>': 'Search for files/directories matching the pattern.',
        'tree': 'Display directory structure as a tree.',
        'find_large <size>': 'Find files larger than the specified size.',
        'log <command>': 'Log the usage of a command to a file.',
        'joke': 'Tell a random joke.'
    }
    for cmd, desc in commands.items():
        print(f"{cmd}: {desc}")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def exit_cli():
    print("Exiting CLI.")
    sys.exit()

def search(pattern):
    matches = [f for f in os.listdir('.') if pattern in f]
    print("\n".join(matches) if matches else "No matches found.")

def tree():
    for root, dirs, files in os.walk("."):
        level = root.replace(".", "").count(os.sep)
        indent = " " * 4 * (level)
        print(f"{indent}{os.path.basename(root)}/")
        subindent = " " * 4 * (level + 1)
        for f in files:
            print(f"{subindent}{f}")

def find_large(size):
    size = int(size)
    large_files = [f for f in os.listdir('.') if os.path.isfile(f) and os.path.getsize(f) > size]
    print("\n".join(large_files) if large_files else "No large files found.")

def log(command):
    with open("command_log.txt", "a") as log_file:
        log_file.write(command + "\n")
    print(f"Logged command: {command}")

def joke():
    jokes = [
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I told my computer I needed a break, and now it won't stop sending me ads for vacation packages.",
        "Why do programmers prefer dark mode? Because light attracts bugs!"
    ]
    print(random.choice(jokes))

def main():
    while True:
        command = input("cli> ").strip().split()
        if not command:
            continue
        cmd = command[0]
        
        if cmd == "ls":
            ls()
        elif cmd == "pwd":
            pwd()
        elif cmd == "cd":
            if len(command) > 1:
                cd(command[1])
            else:
                print("Usage: cd <dir>")
        elif cmd == "mkdir":
            if len(command) > 1:
                mkdir(command[1])
            else:
                print("Usage: mkdir <dir>")
        elif cmd == "rmdir":
            if len(command) > 1:
                rmdir(command[1])
            else:
                print("Usage: rmdir <dir>")
        elif cmd == "touch":
            if len(command) > 1:
                touch(command[1])
            else:
                print("Usage: touch <file>")
        elif cmd == "rm":
            if len(command) > 1:
                rm(command[1])
            else:
                print("Usage: rm <file>")
        elif cmd == "cp":
            if len(command) > 2:
                cp(command[1], command[2])
            else:
                print("Usage: cp <src> <dest>")
        elif cmd == "mv":
            if len(command) > 2:
                mv(command[1], command[2])
            else:
                print("Usage: mv <src> <dest>")
        elif cmd == "help":
            help_cmd()
        elif cmd == "clear":
            clear()
        elif cmd == "exit":
            exit_cli()
        elif cmd == "search":
            if len(command) > 1:
                search(command[1])
            else:
                print("Usage: search <pattern>")
        elif cmd == "tree":
            tree()
        elif cmd == "find_large":
            if len(command) > 1:
                find_large(command[1])
            else:
                print("Usage: find_large <size>")
        elif cmd == "log":
            if len(command) > 1:
                log(" ".join(command[1:]))
            else:
                print("Usage: log <command>")
        elif cmd == "joke":
            joke()
        else:
            print(f"Command '{cmd}' not recognized. Type 'help' for a list of commands.")

if __name__ == "__main__":
    main()