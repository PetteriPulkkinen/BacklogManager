'''
Created by Petteri Pulkkinen
Date 6.6.2018

This file is used to contain main funtion for program execution
'''

import sys
from PyQt5.QtWidgets import QApplication
from manager_gui import ManagerGUI, TaskWidget


def getUserInput(m):
    inp = input("Command: ").split(' ')
    cmd = inp[0]
    try:
        arg1 = inp[1]
        arg2 = inp[2]
    except IndexError:
        pass
    if cmd == 'p':
        m.bl_widget.printTasks()
    elif cmd == 'a':
        m.bl_widget.addTask(TaskWidget(arg1))
    elif cmd == 'c':
        if arg2 == '0':
            m.bl_widget.getTask(arg1).proposeTask()
        if arg2 == '1':
            m.bl_widget.getTask(arg1).startTask()
        elif arg2 == '2':
            m.bl_widget.getTask(arg1).finishTask()
    elif cmd == 'd':
        m.bl_widget.removeTask(arg1)
    else:
        return 0

    return True


if __name__ == '__main__':

    app = QApplication(sys.argv)

    gui = ManagerGUI()

    sys.exit(app.exec_())
