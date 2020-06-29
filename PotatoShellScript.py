import os
import re
import random
import webbrowser
import winsound
from colorama import Fore, Style, Back
from colorama import init
import socket
import Potato_shell.Banner as Banner
import Potato_shell.Help as Help
import Potato_shell.logging as logging
import Potato_shell.send as send
import Potato_shell.license as license

init(convert=True)

normal = os.getcwd()

Banner.banner_read(normal)


def main():
    while True:
        command_input = input(os.getlogin() + "@" + socket.gethostname() + " : " + os.getcwd() + " >")
        if command_input == "help()":
            Help.help_text()

        elif command_input == "license()":
            license.license_show()
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
            except FileExistsError:
                print("ERROR - file already exists")
            except FileNotFoundError:
                print("ERROR - directory doesn't exist")

        elif command_input.startswith("mkdir"):
            string = re.sub(r'^\W*\w+\W*', '', command_input)
            try:
                os.mkdir(string)
                print("Directory made")
            except FileNotFoundError:
                print("ERROR - path doesn't exist")

        elif command_input.startswith("dlt"):
            try:
                os.remove(re.sub(r'^\W*\w+\W*', '', command_input))
                print("File removed")
            except FileNotFoundError:
                print("ERROR - file couldn't be found")

        elif command_input.startswith("dldir"):
            try:
                os.removedirs(re.sub(r'^\W*\w+\W*', '', command_input))
                print("Directory removed")
            except OSError:
                print("ERROR - OSError")

        elif command_input == "cmd()":
            try:
                os.startfile("C:/Windows/System32/cmd.exe")
                print("cmd started")
            except FileNotFoundError:
                print("ERROR - file does not exist or it's in another directory")

        elif command_input.startswith("strt"):
            string = re.sub(r'^\W*\w+\W*', '', command_input)
            try:
                os.startfile(string)
                print("File started")
            except FileNotFoundError:
                print("ERROR - file could not be found")

        elif command_input == "calc()":
            try:
                os.startfile("C:/Windows/System32/calc.exe")
                print("Calculator started")
            except FileNotFoundError:
                print("ERROR - file does not exist or it's in another directory")

        elif command_input.startswith("web"):
            url = re.sub(r'^\W*\w+\W*', '', command_input)
            webbrowser.open(url)
            print("Web site opened")

        elif command_input.startswith("incognito"):
            try:
                url = re.sub(r'^\W*\w+\W*', '', command_input)
                chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
                webbrowser.get(chrome_path).open_new(url)
                print("Website opened with incognito")
            except FileNotFoundError:
                print("ERROR - Chrome couldn't be found")

        elif command_input.startswith("freq"):
            try:
                freq_array = command_input.split(" ")
                length = freq_array[2]
                freq = freq_array[1]
            except IndexError:
                print("ERROR - index error: list index out of range")

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
            except FileNotFoundError:
                print("ERROR - file couldn't be found")
            except:
                print("ERROR - history couldn't be printed")

        elif command_input == "h.erase()":
            try:
                history = open(normal + "/log/history.txt", "w")
                history.write("")
                print("History erased")
            except FileNotFoundError:
                print("ERROR - file not found")
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
                print(Style.RESET_ALL + "")
                files = [f for f in os.listdir('.') if os.path.isfile(f)]
                for f in files:
                    print(Fore.LIGHTGREEN_EX + f)

                print(Style.RESET_ALL)

                dirs = [d for d in os.listdir('.') if os.path.isdir(d)]
                for d in dirs:
                    print(Fore.LIGHTBLUE_EX + d)
                print(Style.RESET_ALL)

            except:
                print("ERROR - couldn't list any files/folders in this directory")

        elif command_input == "cpunum()":
            try:
                print("Number of CPUs:")
                print(os.cpu_count())
            except:
                print("ERROR - couldn't count your CPUs")

        elif command_input == "note()":
            try:
                os.startfile("C:/Windows/notepad.exe")
                print("Notepad opened")
            except:
                print("ERROR - Notepad.exe couldn't be run")

        elif command_input == "exp()":
            try:
                os.startfile("C:/Windows/explorer.exe")
                print("Windows explorer opened")
            except:
                print("ERROR - windows explorer couldn't be opened")

        elif command_input == "fg.green()":
            print(Fore.GREEN + "Text is now green")

        elif command_input == "fg.blue()":
            print(Fore.BLUE + "Text is now blue")

        elif command_input == "c.reset()":
            print(Fore.RESET, Back.RESET + "Text is now normal")

        elif command_input == "cls()":
            def clear():
                os.system('cls')
            clear()
            Banner.banner_read(normal)

        elif command_input.startswith("cat"):
            string = re.sub(r'^\W*\w+\W*', '', command_input)
            try:
                file = open(string, "r")
                print(file.read())
            except FileNotFoundError:
                print("ERROR - file not found")

        elif command_input.startswith("fwrite "):
            try:
                string_without_fwrite = re.sub('fwrite ', '', command_input)

                string_array = string_without_fwrite.split(" ")
                old_path = string_array[0]
                path = string_array[0].replace("~", " ")
                str_array_path = string_array
                str_array_path.remove(old_path)

                file = open(path, "a")
                for i in string_array:
                    file.write(i.replace("$", "\n") + " ")
                file.close()
            except FileNotFoundError:
                print("ERROR - no such directory")
            except UnicodeEncodeError:
                print("ERROR - unicode encode error. Can't use that symbol")

        elif command_input == "gsend()":
            mail = input("email>")
            password = input("password>")
            receiver = input("receiver>")
            subject = input("subject>")
            message = input("message>")
            file_location = input("file location>")
            try:
                send.sending(mail, password, receiver, subject, message, file_location)
            except:
                print("ERROR - the email couldn't be sent")

        elif command_input == "mhelp()":
            webbrowser.open("https://docs.python.org/3/library")
            print("Python docs opened")

        elif command_input == ".ins()":
            try:
                cwf = os.path.basename(__file__)
                os.startfile(cwf)
            except FileNotFoundError:
                print("ERROR - file does not exist")

        elif command_input == "tasklist()":
            os.system("tasklist")

        elif command_input == "tree()":
            os.system("tree")

        elif command_input.startswith("tkill"):
            try:
                os.system("taskkill" + command_input.replace("tkill", ""))
            except:
                print("ERROR")
        else:
            print("Command '" + command_input + "' does not exist")

        logging.writing(command_input, normal)


main()