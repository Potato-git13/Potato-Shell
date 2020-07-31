import os
import re
import random
import webbrowser
import winsound
import socket
import Potato_shell.banner as banner
import Potato_shell.help as help
import Potato_shell.logger as logging
import Potato_shell.send as send
import Potato_shell.license as license
import time
import Potato_shell.music_bot as mb
import hashlib
import Potato_shell.audio_log as al

normal = os.getcwd()

banner.banner_read(normal)


def main():
    while True:
        command_input = input(os.getlogin() + "@" + socket.gethostname() + " : " + os.getcwd() + " \n$ ")
        if command_input == "help()":
            help.help_text()

        elif command_input == "license()":
            license.license_show()

        elif command_input.startswith("echo"):
            text_to_echo = re.sub("echo ", "", command_input)
            if text_to_echo == "%PATH%":
                print(os.getcwd())
            else:
                print(text_to_echo)

        elif command_input.startswith("pecho"):
            try:
                print(re.sub("pecho ", '', command_input))
                try:
                    f = open(normal + "/p echo file.txt", "x")
                except FileExistsError:
                    f = open(normal + "/p echo file.txt", "a")

                f.write(re.sub("pecho ", '', command_input) + "\n")
            except UnicodeEncodeError:
                f.write("UnicodeError")
                print("ERROR - input couldn't be writen in the file")
            f.close()

        elif command_input == "exit()":
            exit()

        elif command_input.startswith("rpass"):
            strng = re.sub("rpass ", '', command_input)
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
                    return ''.join(random.choice(letters) for a in range(string_length))

                num = 0
                while num < 1:
                    print(f"{random_string(int(strng))}")
                    num += 1
            except ValueError:
                print("ERROR - value error char cannot be converted to an integer")

        elif command_input.startswith("mkfile"):
            strng = re.sub("mkfile ", '', command_input)
            try:
                open(strng, "x")
                print("File made")
            except FileExistsError:
                print("ERROR - file already exists")
            except FileNotFoundError:
                print("ERROR - directory doesn't exist")

        elif command_input.startswith("mkdir"):
            strng = re.sub("mkdir ", '', command_input)
            try:
                os.mkdir(strng)
                print("Directory made")
            except FileNotFoundError:
                print("ERROR - path doesn't exist")

        elif command_input.startswith("dlt"):
            try:
                os.remove(re.sub("dlt ", '', command_input))
                print("File removed")
            except FileNotFoundError:
                print("ERROR - file couldn't be found")

        elif command_input.startswith("dltdir"):
            try:
                os.removedirs(re.sub("dltdir ", '', command_input))
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
            strng = re.sub("strt ", '', command_input)
            try:
                os.startfile(strng)
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
            url = re.sub("web ", '', command_input)
            webbrowser.open(url)
            print("Web site opened")

        elif command_input.startswith("incognito"):
            try:
                url = re.sub("incognito ", '', command_input)
                chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
                webbrowser.get(chrome_path).open_new(url)
                print("Website opened with incognito")
            except FileNotFoundError:
                print("ERROR - Chrome couldn't be found")

        elif command_input.startswith("search "):
            search = re.sub("search ", "", command_input)
            webbrowser.open_new("https://google.com/search?q=" + search.replace(" ", "+"))
            print("searched for " + search)

        elif command_input.startswith("isearch "):
            try:
                search = re.sub("isearch ", "", command_input)
                chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
                webbrowser.get(chrome_path).open_new("https://google.com/search?q=" + search.replace(" ", "+"))
                print("searched for " + search + " in incognito mode")
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
            except ValueError:
                print("ERROR - freq is either to low or to high")

        elif command_input == "gith()":
            webbrowser.open("https://github.com")
            print("Github opened")

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

        elif command_input == "h.erase()":
            try:
                history = open(normal + "/log/history.txt", "w")
                history.write("")
                print("History erased")
            except FileNotFoundError:
                print("ERROR - file not found")
            except OSError:
                print("ERROR - history couldn't be erased")

        elif command_input.startswith("cd"):
            strng = re.sub("cd ", '', command_input)
            try:
                os.chdir(strng)
            except FileNotFoundError:
                print("ERROR - directory doesn't exist")
            except PermissionError:
                print("ERROR - you are not permitted to switch to this directory: " + strng)

        elif command_input == "ls()":
            try:
                print("")

                files = [f for f in os.listdir('.') if os.path.isfile(f)]
                for f in files:
                    print(f)

                print("")

                dirs = [d for d in os.listdir('.') if os.path.isdir(d)]
                for d in dirs:
                    print(d)

                print("")
            except PermissionError:
                print("ERROR - you are not permitted to see files in this directory")

        elif command_input == "cpunum()":
            print("Number of CPUs:")
            print(os.cpu_count())

        elif command_input == "note()":
            try:
                os.startfile("C:/Windows/notepad.exe")
                print("Notepad opened")
            except FileNotFoundError:
                print("ERROR - Notepad.exe couldn't found")

        elif command_input == "exp()":
            try:
                os.startfile("C:/Windows/explorer.exe")
                print("Windows explorer opened")
            except FileNotFoundError:
                print("ERROR - windows explorer couldn't be found")

        elif command_input == "cls()":
            def clear():
                os.system('cls')

            clear()
            banner.banner_read(normal)

        elif command_input.startswith("cat"):
            strng = re.sub("cat ", '', command_input)
            try:
                file = open(strng, "r")
                print(file.read())
            except FileNotFoundError:
                print("ERROR - file not found")
            except PermissionError:
                print("ERROR - you are not permitted to see the contents of this file")

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
            import Potato_shell.pass_to_asterisks as pta
            try:
                password = pta.getpass("password>")
            except KeyboardInterrupt:
                print("\nCan't use Ctrl + C!")
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
            os.system("taskkill" + command_input.replace("tkill", ""))

        elif command_input.startswith("color"):
            os.system("color " + re.sub("color ", "", command_input))

        elif command_input == "time()":
            print("The current time is: " + time.strftime("%Y:%m:%d:%H:%M:%S"))

        elif command_input == "mb()":
            try:
                mb.music()
            except FileNotFoundError:
                print("ERROR - file was not found")

        elif command_input.startswith("md5 "):
            try:
                strng = re.sub("md5 ", "", command_input)
                string_b = hashlib.md5(strng.encode())
                print(string_b.hexdigest())
            except:
                print("ERROR - text couldn't be encoded")

        elif command_input.startswith("audio.log"):
            try:
                al.log(command_input)
            except ValueError:
                print("ERROR - input wasn't a number")

        elif command_input == "unicode()":
            webbrowser.open("https://www.rapidtables.com/code/text/unicode-characters.html")
            print("Unicode table opened")

        elif command_input == "potatoenc()":
            import Potato_shell.potato_encoding as penc
            try:
                penc.potatoes()
                print("Started the encryption module")
            except:
                print("ERROR - something went wrong")

        elif command_input.startswith("sudo "):
            file_path = re.sub("sudo ", "", command_input)
            os.system('runas /profile /user:administrator "' + file_path + '"')

        elif command_input.startswith("cmd "):
            command = re.sub("cmd ", "", command_input)
            os.system(command)

        else:
            print("Command '" + command_input + "' does not exist")

        logging.writing(command_input, normal)


os.system("title Potato shell")
main()
