from pynput.keyboard import Key, Controller
import os
import sys
import re
from time import sleep, time
from lib import TYPER


def type(txteditor, killkey, kill=False):
    keybrd = Controller()
    sleep(2)
    os.system(f"{txteditor} " + os.getcwd() + f"/{TYPER}")
    sleep(1)
    line = 0
    while kill is False:
        sleep(1)
        for num in range(80):
            keybrd.press(".")
            sleep(0.1)

            # try:
            # if kbrd.read_key(killkey) or kbrd.read_key(killkey.upper()):
            keybrd.press(Key.ctrl)
            keybrd.press("s")
            sleep(0.1)
            keybrd.release(Key.ctrl)
            keybrd.release("s")
            # print(f"\nHot key [{killkey}] was pressed\n")
            # sys.exit()

            # f = open(TYPER, "r").readlines()
            # killkey = re.search(r"x|X", f[line])
            # if killkey:
            #     keybrd.press(Key.ctrl)
            #     keybrd.press("s")
            #     sleep(0.1)
            #     keybrd.release(Key.ctrl)
            #     keybrd.release("s")
            #     print(f"\nHot key [{killkey.group()}] was pressed\n")
            #     sys.exit()
            # else:
            #     continue
        line += 1
        keybrd.release(".")
        keybrd.press(Key.enter)
        keybrd.release(Key.enter)


if __name__ == "__main__":
    pass
