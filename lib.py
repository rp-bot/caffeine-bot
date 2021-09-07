import datetime

operating_systems = {"1": "Windows", "2": "Linux", "3": "Mac"}

def_text_editor = {"Windows": "Notepad", "Linux": "gedit", "Mac": "TextEdit"}

tdy = datetime.date.today().strftime("%d-%b-%y")
config_r = open("preferences.cfg", "r").readlines()
# config_w = open("preferences.cfg", "w+")
typer = open(f"typer_{tdy}", "w+")
