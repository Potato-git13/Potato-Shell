from enc_and_dec_potato.encoding import encode
from enc_and_dec_potato.decoding import decode
from cryptography.fernet import Fernet


def potatoes():
    not_exit = True

    while not_exit:

        choice = input(">")

        if choice == "enc":
            text = input("encode: ")
            key_to_use = input("key: ")
            encoded = encode(text, key_to_use).decode("utf-8")
            print(encoded)
            write_to_file = input("Should I write this to a file?(y/n)")
            if write_to_file == "y":
                print("Saved")
                try:
                    f = open("encoded.txt", "x")
                    f.write(encoded + "\n")
                except FileExistsError:
                    f = open("encoded.txt", "a")
                    f.write(encoded + "\n")
            else:
                print("Ok")

        elif choice == "dec":
            text = input("decode: ")
            key_to_use = input("key: ")
            decoded = decode(text, key_to_use).decode("utf-8")
            print(decoded)
            write_to_file = input("Should I write this to a file?(y/n)")
            if write_to_file == "y":
                print("Saved")
                try:
                    f = open("decoded.txt", "x")
                    f.write(decoded + "\n")
                except FileExistsError:
                    f = open("decoded.txt", "a")
                    f.write(decoded + "\n")
            else:
                print("Ok")

        elif choice == "newkey":
            print(Fernet.generate_key().decode("utf-8"))

        elif choice == "exit":
            not_exit = False

        else:
            print("Couldn't understand that....")
