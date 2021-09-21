import os
import lib
from time import sleep


def cfg():
    OPERATING_SYSTEM = ""
    CONFIRMATION = False
    YN = ("y", "n")
    while CONFIRMATION is False and OPERATING_SYSTEM == "":
        OPERATING_SYSTEM = input(
            """choose your OS\n1 for Windows,\n2 for Linux,\n3 for mac\n"""
        )
        try:
            print("""You chose """ + lib.OPERATING_SYSTEMS[OPERATING_SYSTEM])
            sleep(0.5)
        except KeyError:
            print("please enter the right number")
            OPERATING_SYSTEM = ""
        else:
            while CONFIRMATION is False:
                confirmation_input = ""
                confirmation_input = input(
                    "Do you wish to keep the changes [Y/N]: "
                ).lower()
                if confirmation_input in YN:
                    if confirmation_input == "y":
                        lib.writeconf_OS(lib.OPERATING_SYSTEMS[OPERATING_SYSTEM])
                        print(
                            "the default text editor will be "
                            + lib.TEXT_EDITORS[lib.OPERATING_SYSTEMS[OPERATING_SYSTEM]]
                            + "."
                        )
                        confirmation_input = ""
                        while confirmation_input not in YN:
                            confirmation_input = input(
                                "Do you wish to keep it [Y/N]: "
                            ).lower()
                            if confirmation_input == "y":
                                CONFIRMATION = True
                            elif confirmation_input == "n":
                                txteditor = "1"
                                while txteditor.isdigit() is True:
                                    txteditor = input(
                                        """please enter the CORRECT name of the 
                                        text editor you wish to change to: """
                                    )
                                    if txteditor.isdigit() is True:
                                        continue
                                    else:
                                        lib.writeconf_TXT(txteditor)
                            else:
                                continue
                        break
                    elif confirmation_input == "n":
                        print("You can try again!")
                        OPERATING_SYSTEM = ""
                        sleep(0.5)
                        break
                else:
                    print("please! type Y or N")

    while CONFIRMATION is True:
        os.system("clear")
        save = ""
        while save not in YN:
            save = input("\nDon't ask Again? [Y/N]: ").lower()
            if save == "y":
                lib.writeconf_CONF("True")
                print("Done!")
                print("your current preferences are: \n")
                for i in range(0, len(lib.CFG_R)):
                    print(lib.CFG_R[i])
                print("\n")
                CONFIRMATION = False
                break
            elif save == "n":
                print("Done!")
                CONFIRMATION = False


if __name__ == "__main__":
    pass
