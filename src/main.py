'''
Created by Petteri Pulkkinen
Date 6.6.2018

This file is used to contain main funtion for program execution
'''

from manager_gui import *
import sys
from PyQt5.QtWidgets import QApplication

'''
def getUserInput():
    inp = input("Command: ").split(' ')
    cmd = inp[0]
    arg = ""
    try:
        arg1 = inp[1]
        arg2 = inp[2]
    except:
        pass
    if cmd == 'p':
        m.backlog.print_items()
    elif cmd == 'a':
        m.backlog.add_task(Task(arg1))
    elif cmd == 'c':
        if arg2 == '0':
            m.backlog.get_task(arg1).propose_task()
        if arg2 == '1':
            m.backlog.get_task(arg1).start_task()
        elif arg2 == '2':
            m.backlog.get_task(arg1).finish_task()
    elif cmd == 'd':
        m.backlog.remove_task(arg1)
    else:
        return 0

    return True
    '''

if __name__ == '__main__':

    app = QApplication(sys.argv)

    gui = ManagerGUI()

    sys.exit(app.exec_())
