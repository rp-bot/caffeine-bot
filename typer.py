from pynput.keyboard import Key, KeyCode, Listener, Controller
from time import sleep
from lib import TDY


def type():
    keybrd = Controller()
    cut = 0
    sleep(1)
    while cut < 4:
        for num in range(80):
            keybrd.press(".")
            sleep(0.1)
        keybrd.release(".")
        keybrd.press(Key.enter)
        keybrd.release(Key.enter)
        cut += 1


SHORTCUTS = [{KeyCode(char="a")}, {KeyCode(char="A")}]
CURRENT = set()


def execute():
    pass


def on_press(key):
    if any([key in cut for cut in SHORTCUTS]):
        CURRENT.add(key)
        if any(all(k in CURRENT for k in cut) for cut in SHORTCUTS):
            execute()


def on_release(key):
    if any([key in cut for cut in SHORTCUTS]):
        CURRENT.remove(key)


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

