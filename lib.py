import datetime
import re
import sys
import os
from time import sleep
from pynput.keyboard import Key, Controller, KeyCode, Listener
# from hotkeylistener import hotkey_scan

OPERATING_SYSTEMS = {"1": "Windows", "2": "Linux", "3": "Mac"}

TEXT_EDITORS = {"Windows": "Notepad", "Linux": "gedit", "Mac": "TextEdit"}
TDY = datetime.date.today().strftime("%d-%b-%y")
TYPER = f"diarrhea/typer_{TDY}.txt"
F = open(TYPER, "w+")
CFG_R = open("preferences.cfg", "r").readlines()
EXPR = r"(?<=\')(.*?)(?=\')"


def writeconf_OS(OS):
    os = re.findall(r"(?<=\'){}(?=\')".format(OS), CFG_R[0])
    if os:
        pass
    else:
        CFG_R[0] = re.sub(EXPR, OS, CFG_R[0])
        CFG_R[1] = re.sub(EXPR, TEXT_EDITORS[OS], CFG_R[1])
    cfg_w = open("preferences.cfg", "w+")
    cfg_w.writelines(CFG_R)
    cfg_w.close()


def writeconf_TXT(TXT):
    txt = re.findall(r"(?<=\'){}(?=\')".format(TXT), CFG_R[1])
    if txt:
        pass
    else:
        CFG_R[1] = re.sub(EXPR, TXT, CFG_R[1])
    cfg_w = open("preferences.cfg", "w+")
    cfg_w.writelines(CFG_R)
    cfg_w.close()


def writeconf_CONF(CONF):
    CFG_R[3] = re.sub(EXPR, CONF, CFG_R[3])
    cfg_w = open("preferences.cfg", "w+")
    cfg_w.writelines(CFG_R)
    cfg_w.close()


class ReadConf:
    def __init__(self):
        self.os = re.search(EXPR, CFG_R[0])
        self.txt = re.search(EXPR, CFG_R[1])
        self.killkey = re.search(EXPR, CFG_R[2])
        self.conf = re.search(EXPR, CFG_R[3])

    def savecheck(self):
        try:
            return self.conf.group()
        except AttributeError:
            print("\n.cfg error\n")
            sys.exit()

    def KillKey(self):
        try:
            return self.killkey.group().lower()
        except AttributeError:
            print("\n.cfg error\n")
            sys.exit()

    def TXT(self):
        try:
            return self.txt.group()
        except AttributeError:
            print("\n.cfg error\n")
            sys.exit()

    def OS(self):
        try:
            return self.os.group()
        except AttributeError:
            print("\n.cfg error\n")
            sys.exit()


savecheck = ReadConf().savecheck()
killkey = ReadConf().KillKey()
txteditor = ReadConf().TXT()
OS = ReadConf().OS()
KEYBOARD = Controller()
SHORTCUTS = [{KeyCode(char=killkey.lower())}, {KeyCode(char=killkey.upper())}]
CURRENT = set()
KILL = False


def save(keybrd):
    keybrd.press(Key.ctrl)
    keybrd.press("s")
    sleep(0.1)
    keybrd.release(Key.ctrl)
    keybrd.release("s")


def hotkey_scan():
    def execute(key):
        global KILL, killkey
        KILL = True
        killkey = key

    def on_press(key):

        if any([key in cut for cut in SHORTCUTS]):
            CURRENT.add(key)
            if any(all(k in CURRENT for k in cut) for cut in SHORTCUTS):
                execute(key)

    def on_release(key):
        if any([key in cut for cut in SHORTCUTS]):
            CURRENT.remove(key)

    listener = Listener(on_press=on_press, on_release=on_release)
    listener.start()
    sleep(0.5)


def type():
    global KILL, killkey
    keybrd = Controller()
    sleep(2)
    os.system(f"{txteditor} " + os.getcwd() + f"/{TYPER}")
    sleep(2)
    line = 0
    while KILL is False:
        for num in range(80):
            keybrd.tap(".")
            sleep(0.1)
            hotkey_scan()
            if KILL == True:
                os.system("clear")
                print(f"\nKill key [{killkey}] was pressed\n")
                break
        line += 1
        keybrd.press(Key.enter)
        keybrd.release(Key.enter)
        save(KEYBOARD)


if __name__ == "__main__":
    pass
