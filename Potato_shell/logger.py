# A module for logging the usage of the Potato shell


import time
import os


def writing(command_input, normal_path):
    try:
        os.makedirs(normal_path + "/log")
    except FileExistsError:
        pass
    try:
        file = open(normal_path + "/log/history.txt", "x")
    except:
        file = open(normal_path + "/log/history.txt", "a")
    try:
        file.write(time.strftime("%Y:%m:%d:%H:%M:%S") + " - " + command_input + "\n")
    except UnicodeEncodeError:
        file.write(time.strftime("%Y:%m:%d:%H:%M:%S") + " - UnicodeEncodeError\n")
    file.close()
