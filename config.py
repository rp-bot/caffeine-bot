import os
import lib
from time import sleep


operating_system = ""
confirmation = False
YorN = ("y", "n")
while confirmation is False and operating_system == "":
    operating_system = input(
        '''choose your OS\n1 for Windows,\n2 for Linux,\n3 for mac\n''')
    try:
        print('''You chose ''' + lib.operating_systems[operating_system])
        sleep(.5)
    except KeyError:
        print("please enter the right number")
        operating_system = ""
    else:
        while confirmation is False:
            confirmation_input = ''
            confirmation_input = input(
                "Do you wish to keep the changes [Y/N]: ").lower()
            if confirmation_input in YorN:
                if confirmation_input == "y":
                    lib.writeconf_OS(lib.operating_systems[operating_system])
                    print("the default text editor will be " + lib.def_text_editor[lib.operating_systems[operating_system]]+".")
                    confirmation_input = ""
                    while confirmation_input not in YorN:
                        confirmation_input = input(
                        "Do you wish to keep it [Y/N]: ").lower()
                        if confirmation_input == 'y':
                            confirmation = True
                        elif confirmation_input == 'n':
                            txteditor = "1"
                            while txteditor.isdigit() is True:
                                txteditor = input("please enter the CORRECT name of the text editor you wish to change to: ")
                                if txteditor.isdigit() is True:
                                    continue
                                else:
                                    lib.writeconf_TXT(txteditor)
                        else:
                            continue
                    break
                elif confirmation_input == "n":
                    print("You can try again!")
                    operating_system = ""
                    sleep(.5)
                    break
            else:
                print("please! type Y or N")
    #
    # print(os.getcwd())
    # os.s6ystem("gedit " + os.getcwd() + "/preferences.cfg")
