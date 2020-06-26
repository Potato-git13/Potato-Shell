# A module that displays the banner from the read file
import os
normal = os.getcwd()


def banner_read():
    try:
        banner = open(normal + "/.banner", "r")
        print(banner.read())
    except:
        print("ERROR - the banner couldn't be loaded")
    print("\nType help() for the list of commands")