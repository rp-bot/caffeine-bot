from time import sleep
from lib import TYPER, F, CFG_R, EXPR, type, savecheck, killkey
from config import cfg
import os


if __name__ == "__main__":
    if savecheck.lower() == "false":
        cfg()

    elif savecheck.lower() == "true":
        os.system("clear")
        print(f"hit [{killkey}] when you wish to quit")
        sleep(.5)
        type()
