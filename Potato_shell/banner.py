# A module that displays the banner from the read file


def banner_read(default_path):
    try:
        banner = open(default_path + "/.banner", "r")
        print(banner.read())
    except FileNotFoundError:
        print("ERROR - the banner does not exist")
    print("\nType help() for the list of commands")
