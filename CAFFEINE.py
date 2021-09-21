from lib import TYPER, F, CFG_R, EXPR, ReadConf
from config import cfg
from typer import type
import os

#
# print(os.getcwd())
# os.s6ystem("gedit " + os.getcwd() + "/preferences.cfg")

savecheck = ReadConf().savecheck()
killkey = ReadConf().KillKey()
txteditor = ReadConf().TXT()
# if savecheck == "False":
#     cfg()

# if savecheck == "True":
#     os.system("clear")
#     print(f"hit [{killkey}] when you wish to quit")
#     # .os.system("python3 hotkeylistener.pyw")
#     os.system(f"{txteditor} " + os.getcwd() + f"/{TYPER}")
#     type()
