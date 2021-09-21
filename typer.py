from pynput.keyboard import Key, Controller
import os
import sys
import re
from time import sleep, time
from lib import readline, ReadConf, TYPER, FR, F


def type(txteditor, kill=False):
    keybrd = Controller()
    sleep(1)
    os.system(f"{txteditor} " + os.getcwd() + f"/{TYPER}")
    sleep(2)
    line = 0
    while kill is False:
        for num in range(80):
            keybrd.press(".")
            sleep(0.1)
            keybrd.press(Key.ctrl)
            keybrd.press("s")
            sleep(0.1)
            keybrd.release(Key.ctrl)
            keybrd.release("s")
            f = open(TYPER, "r").readlines()
            killkey = re.search(r"x|X", f[line])
            if killkey:
                print(f"\nHot key [{killkey.group()}] was pressed\n")
                sys.exit()
            else:
                continue
        line += 1
        keybrd.release(".")
        keybrd.press(Key.enter)
        keybrd.release(Key.enter)


if __name__ == "__main__":
    type()
