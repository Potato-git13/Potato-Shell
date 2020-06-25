import os
import re
import random
import time
import webbrowser
import winsound

normal = os.getcwd()

try:
    banner = open(normal + "/.banner", "r")
    print(banner.read())
except:
    print("ERROR - the banner couldn't be loaded")
print("\nType help() for the list of commands")


def main():
    while True:
        command_input = input(os.getlogin() + " : " + os.getcwd() + " >")
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
ushrt()         prints useful shortcuts
web             starts a specified website
freq            plays the input(freq(37 - 32767), length)
gith()          opens github.com
crash()         crashes the console
h.show()        shows your history
h.erase()       erases your history
indir()         prints all the files and folders in the current directory
cd              changes the cdw to the input
ls()            lists all files and directories in the cwd
cpunum()        returns how many CPUs are in the machine""")
        elif command_input.startswith("echo"):
            try:
                print(re.sub(r'^\W*\w+\W*', '', command_input))
            except:
                print("ERROR - input couldn't be printed")

        elif command_input.startswith("pecho"):
            try:
                print(re.sub(r'^\W*\w+\W*', '', command_input))
                try:
                    f = open(normal + "/p echo file.txt", "x")
                except:
                    f = open(normal + "/p echo file.txt", "a")

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

        elif command_input == "ushrt()":
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

        elif command_input.startswith("freq"):
            freq_array = command_input.split(" ")
            length = freq_array[2]
            freq = freq_array[1]

            try:
                print(f"Playing {freq} for {length} seconds")

                length = int(length) * 1000
                winsound.Beep(int(freq), length)
            except:
                print("ERROR - frequency couldn't be played")

        elif command_input == "gith()":
            try:
                webbrowser.open("https://github.com")
                print("GitHub opened")
            except:
                print("ERROR - GitHub couldn't be opened")

        elif command_input == "crash()":
            crash = "string"
            print(int(crash))

        elif command_input == "h.show()":
            try:
                history = open(normal + "/log/history.txt", "r")
                print("Your history:\n")
                print(history.read())
                history.close()
            except:
                print("ERROR - history couldn't be printed")

        elif command_input == "h.erase()":
            try:
                history = open(normal + "/log/history.txt", "w")
                history.write("")
                print("History erased")
            except:
                print("ERROR - history couldn't be erased")

        elif command_input.startswith("cd"):
            string = re.sub(r'^\W*\w+\W*', '', command_input)
            try:
                os.chdir(string)
            except:
                print("ERROR - couldn't go to this directory")

        elif command_input == "ls()":
            try:
                print("")
                files = [f for f in os.listdir('.') if os.path.isfile(f)]
                for f in files:
                    print(f)
                print("")
            except:
                print("ERROR - couldn't list any files/folders in this directory")

        elif command_input == "cpunum()":
            try:
                print("Number of CPUs:")
                print(os.cpu_count())
            except:
                print("ERROR - couldn't count your CPUs")

        else:
            print("Command '" + command_input + "' does not exist")

        try:
            os.makedirs("log")
        except:
            place_holder = True
        try:
            file = open(normal + "/log/history.txt", "x")
        except:
            file = open(normal + "/log/history.txt", "a")
        file.write(time.strftime("%Y:%m:%d:%H:%M:%S") + " - " + command_input + "\n")
        file.close()


main()
