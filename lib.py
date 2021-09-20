import datetime
import re

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


def readconf():
    os = re.findall(r"(?<=\')(.*?)(?=\')", CFG_R[0])
    txt = re.findall(r"(?<=\')(.*?)(?=\')", CFG_R[1])
