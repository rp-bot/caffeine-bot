from pynput.keyboard import Key, Controller
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

