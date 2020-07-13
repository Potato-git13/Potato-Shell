import webbrowser
from pynput.mouse import Button
from pynput.mouse import Controller as mc
from pynput.keyboard import Controller as kc
from pynput.keyboard import Key
import time


def music():
    try:
        musicList = open("music_list.txt", "r")
    except FileNotFoundError:
        print("File does not exist")

    webbrowser.open("https://music.youtube.com/")
    mouse = mc()
    keyboard = kc()

    time.sleep(3.5)
    mouse.position = (164, 365)
    time.sleep(0.5)
    mouse.click(Button.left, 1)

    time.sleep(2)
    mouse.position = (971, 95)
    time.sleep(0.5)
    mouse.click(Button.left, 1)
    time.sleep(0.5)
    mouse.click(Button.left, 1)
    time.sleep(1)
    keyboard.type(musicList.readline())
    time.sleep(0.5)
    keyboard.press(Key.enter)
    time.sleep(0.5)
    keyboard.release(Key.enter)

    time.sleep(1)
    mouse.position = (1194, 298)
    time.sleep(0.5)
    mouse.click(Button.left, 1)
    time.sleep(0.3)
    mouse.position = (1203, 497)
    time.sleep(0.3)
    mouse.click(Button.left, 1)
    for line in musicList:
        mouse.position = (978, 105)
        time.sleep(0.5)
        mouse.click(Button.left, 1)
        time.sleep(0.3)
        keyboard.press(Key.ctrl)
        keyboard.press("a")
        time.sleep(0.3)
        keyboard.release(Key.ctrl)
        keyboard.release("a")

        keyboard.type(line)
        time.sleep(0.3)
        keyboard.press(Key.enter)
        time.sleep(0.3)
        keyboard.release(Key.enter)

        time.sleep(1)
        mouse.position = (1194, 298)
        time.sleep(0.5)
        mouse.click(Button.left, 1)
        time.sleep(0.4)
        mouse.position = (1203, 497)
        time.sleep(0.3)
        mouse.click(Button.left, 1)

    time.sleep(0.3)
    mouse.position = (1559, 830)
    time.sleep(0.2)
    mouse.click(Button.left, 1)
    time.sleep(1)
    mouse.position = (1027, 295)
    mouse.click(Button.left, 1)
