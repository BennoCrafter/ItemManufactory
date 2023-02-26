import os


def help():
    with open("Documentation/instruction.txt", "r") as ins:
        print(ins.read())
    ins.close()

    # Wait for user input
    input("Press Enter to clear the screen...")

    # Clear the screen
    if os.name == "nt":
        os.system("cls")  # For Windows
    else:
        os.system("clear")  # For Linux and macOS
