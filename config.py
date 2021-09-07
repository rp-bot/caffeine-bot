import os
import lib
from time import sleep
from IPython.display import clear_output


operating_system = ""
confirmation = False
YorN = ["y", "n"]
while confirmation is False and operating_system == "":
    operating_system = input(
        '''choose your OS\n1 for Windows,\n2 for Linux,\n3 for mac\n''')
    try:
        print('''You chose ''' + lib.operating_systems[operating_system])
        sleep(.5)
    except KeyError:
        clear_output()
        print("please enter the right number")
        operating_system = ""
    else:
        while confirmation is False:
            confirmation_input = ''
            confirmation_input = input(
                "Do you wish to keep the changes [Y/N]: ").lower()
            if confirmation_input in YorN:
                if confirmation_input == "y":
                    # overwrite the list and the write to the orignal .cfg
                    print("Done!")
                    confirmation = True
                    break
                elif confirmation_input == "n":
                    print("You can try again!")
                    operating_system = ""
                    sleep(.5)
                    break
            else:
                print("please type Y or N")
    #
    # print(os.getcwd())
    # os.s6ystem("gedit " + os.getcwd() + "/preferences.cfg")
