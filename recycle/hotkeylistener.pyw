from pynput.keyboard import Listener, KeyCode, Key, Controller
from lib import ReadConf, TYPER
from typer import type
import sys
import os
from time import sleep

KEYBOARD = Controller()
HOTKEY = ReadConf().KillKey()

SHORTCUTS = [{KeyCode(char=HOTKEY.lower())}, {KeyCode(char=HOTKEY.upper())}]
CURRENT = set()


def execute(key):
    print(f"\nHot key [{key}] was pressed\n")

    sys.exit()


def on_press(key):

    if any([key in cut for cut in SHORTCUTS]):
        CURRENT.add(key)
        if any(all(k in CURRENT for k in cut) for cut in SHORTCUTS):
            execute(key)


def on_release(key):
    if any([key in cut for cut in SHORTCUTS]):
        CURRENT.remove(key)


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

