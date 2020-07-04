import speech_recognition as sr
import re


def log(command):
    r = sr.Recognizer()
    mic = sr.Microphone()
    i = re.sub("audio.log ", "", command)
    n = 0
    txts = ""
    txt = []
    i = int(i)
    i -= 1
    while n <= i:
        try:
            with mic as source:
                audio = r.listen(source)
            audio_r = r.recognize_google(audio)
            txts = str(audio_r)
            txt.append(txts)
            n += 1
            print(n)

        except sr.UnknownValueError:
            txts = "empty"
            txt.append(txts)
            n += 1
            print(n)

    def l_to_str(l):
        converted = ""
        return converted + " ".join(l)

    end = l_to_str(txt)
    print(end)
    save = input("Should I save this to a file?").lower()
    if save == "yes":
        try:
            file = open("audio.log.txt", "x")
        except FileExistsError:
            file = open("audio.log.txt", "a")
        file.write(end + "\n")
        print("text saved to a file")
        file.close()