import datetime
import re

operating_systems = {"1": "Windows", "2": "Linux", "3": "Mac"}

def_text_editor = {"Windows": "Notepad", "Linux": "gedit", "Mac": "TextEdit"}

tdy = datetime.date.today().strftime("%d-%b-%y")
typer = open(f"typer_{tdy}.txt", "w+")
cfg_r = open("preferences.cfg", "r").readlines()
expr = r"(?<=\')(.*?)(?=\')"
def writeconf_OS(OS):
    os = re.findall(r"(?<=\'){}(?=\')".format(OS),cfg_r[0])
    if os:
        pass
    else:
        cfg_r[0] = re.sub(expr, OS ,cfg_r[0])
        cfg_r[1] = re.sub(expr, def_text_editor[OS],cfg_r[1])
    cfg_w = open("preferences.cfg", "w+")
    cfg_w.writelines(cfg_r)
    cfg_w.close()

def writeconf_TXT(TXT):
    txt = re.findall(r"(?<=\'){}(?=\')".format(TXT),cfg_r[1])
    if txt:
        pass
    else:
        cfg_r[1] = re.sub(expr, TXT,cfg_r[1])
    cfg_w = open("preferences.cfg", "w+")
    cfg_w.writelines(cfg_r)
    cfg_w.close()