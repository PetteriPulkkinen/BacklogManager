'''
Created by Petteri Pulkkinen
Date 6.6.2018

This file is used to contain main funtion for program execution
'''

import sys
from PyQt5.QtWidgets import QApplication
from manager_gui import ManagerGUI

if __name__ == '__main__':

    app = QApplication(sys.argv)

    gui = ManagerGUI()

    sys.exit(app.exec_())
