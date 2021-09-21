from lib import F, CFG_R, EXPR, ReadConf
from config import cfg
from typer import type
import os

#
# print(os.getcwd())
# os.s6ystem("gedit " + os.getcwd() + "/preferences.cfg")
check = ReadConf().savecheck()
if check == "False":
    cfg()


elif check == "True":
    pass
