import os
import re
import random
import time
import webbrowser

print("POTATO SHELL")
print("""=====================================
= Made by Potato man / Potato-git13 =
=====================================""")

print(" ")
print("Type help() for commands.")
print("")


def main():
    while True:
        command_input = input(">")
        if command_input == "help()":
            print("""help()          shows this list
echo            writes the input
pecho           writes the input in to a .txt file
exit()          kills the shell
rpass           generates a random password(input is the len)
mkfile          make a file in a specified path
mkdir           make a directory in a specified path
dlt             delete a file
dldir           delete a directory
strt            opens a specified file
cmd()           starts cmd terminal
calc()          open the calculator
ushrt           prints useful shortcuts
web             starts a specified website""")
        elif command_input.startswith("echo"):
            try:
                print(re.sub(r'^\W*\w+\W*', '', command_input))
            except:
                print("ERROR - input couldn't be printed")

        elif command_input.startswith(("pecho")):
            try:
                print(re.sub(r'^\W*\w+\W*', '', command_input))
                try:
                    f = open("p echo file.txt", "x")
                except:
                    f = open("p echo file.txt", "a")

                f.write(re.sub(r'^\W*\w+\W*', '', command_input) + "\n")
                f.close()
            except:
                print("ERROR - input couldn't be writen in the file")

        elif command_input == "exit()":
            exit()

        elif command_input.startswith("rpass"):
            string = re.sub(r'^\W*\w+\W*', '', command_input)
            try:

                def random_string(string_length=8):
                    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                               'S',
                               'T', 'U',
                               'V', 'W', 'X', 'Y', 'Z',
                               'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                               's',
                               't', 'u',
                               'v', 'w', 'x', 'y', 'z',
                               '1', '2', '3', '4', '5', '6', '7', '8', '9',
                               '!', '"', '#', '$', '%', '&', '/', '(', ')', '=', '?', '*', ',', '.', '-', ';', ':', '_']
                    return ''.join(random.choice(letters) for i in range(string_length))

                rand_num = random.randint(0, 99999)
                num = 0
                while num < 1:
                    print(f"{random_string(int(string))}")
                    num += 1
            except:
                print("ERROR - password couldn't be generated")

        elif command_input.startswith("mkfile"):
            string = re.sub(r'^\W*\w+\W*', '', command_input)
            try:
                open(string, "x")
                print("File made")
            except:
                print("ERROR - couldn't create the file")

        elif command_input.startswith("mkdir"):
            string = re.sub(r'^\W*\w+\W*', '', command_input)
            try:
                os.mkdir(string)
                print("Directory made")
            except:
                print("ERROR - directory couldn't be made")

        elif command_input.startswith("dlt"):
            try:
                os.remove(re.sub(r'^\W*\w+\W*', '', command_input))
                print("File removed")
            except:
                print("ERROR - file couldn't be removed")

        elif command_input.startswith("dldir"):
            try:
                os.removedirs(re.sub(r'^\W*\w+\W*', '', command_input))
                print("Directory removed")
            except:
                print("ERROR - directory couldn't be removed")

        elif command_input == "cmd()":
            try:
                os.startfile("C:/Windows/System32/cmd.exe")
                print("cmd started")
            except:
                print("ERROR - couldn't start cmd")

        elif command_input.startswith("strt"):
            string = re.sub(r'^\W*\w+\W*', '', command_input)
            try:
                os.startfile(string)
                print("File started")
            except:
                print("ERROR - couldn't start the file")

        elif command_input == "calc()":
            try:
                os.startfile("C:/Windows/System32/calc.exe")
                print("Calculator started")
            except:
                print("ERROR - couldn't start the calculator")

        elif command_input == "ushrt":
            print("MC")
            print("D:/.minecraft/Launcher.exe")
            print("PS")
            print("C:/Program Files/Adobe/Adobe Photoshop CC 2019/Photoshop.exe")
            print("Discord")
            print("C:/Users/matevz/AppData/Local/Discord/app-0.0.306/Discord.exe")
            print("VS Code")
            print("C:/Users/matevz/AppData/Local/Programs/Microsoft VS Code/Code.exe")

        elif command_input.startswith("web"):
            string = re.sub(r'^\W*\w+\W*', '', command_input)
            try:
                webbrowser.open(string)
                print("Web site opened")
            except:
                print("ERROR - the web site couldn't be opened")

        else:
            print("Command '" + command_input + "' does not exist")

        try:
            os.makedirs("log")
        except:
            poop = "poop"
        try:
            file = open("log/history.txt", "x")
        except:
            file = open("log/history.txt", "a")
        file.write(time.strftime("%Y:%m:%d:%H:%M:%S") + " - " + command_input + "\n")
        file.close()


main()
