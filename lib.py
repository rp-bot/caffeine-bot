import datetime
import re
import sys
import os
from time import sleep
from pynput.keyboard import Key, Controller

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
            return self.killkey.group()
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


def type(txteditor, kill=False):
    keybrd = Controller()
    sleep(2)
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
    pass

