import datetime
import re
import sys

OPERATING_SYSTEMS = {"1": "Windows", "2": "Linux", "3": "Mac"}

TEXT_EDITORS = {"Windows": "Notepad", "Linux": "gedit", "Mac": "TextEdit"}
TDY = datetime.date.today().strftime("%d-%b-%y")
F = open(f"typer_{TDY}.txt", "w+")
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
            sys.exit("\n.cfg error\n")

    def KillKey(self):
        try:
            return self.killkey.group()
        except AttributeError:
            sys.exit("\n.cfg error\n")

