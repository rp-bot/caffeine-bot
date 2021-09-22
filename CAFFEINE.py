from lib import TYPER, F, CFG_R, EXPR, type, ReadConf
from config import cfg

# from typer import type
import os

#
# print(os.getcwd())
# os.s6ystem("gedit " + os.getcwd() + "/preferences.cfg")

savecheck = ReadConf().savecheck()
killkey = ReadConf().KillKey()
txteditor = ReadConf().TXT()
OS = ReadConf().OS()
if savecheck.lower() == "false":
    cfg()

elif savecheck.lower() == "true":
    os.system("clear")
    print(f"hit [{killkey}] when you wish to quit")
    type(txteditor)
    os.system("clear")
