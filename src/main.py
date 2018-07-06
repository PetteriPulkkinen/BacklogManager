'''
Created by Petteri Pulkkinen
Date 6.6.2018

This file is used to contain main funtion for program execution
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':

    app = QApplication(sys.argv)

    app_window = QWidget()
    app_window.setWindowTitle('Backlog manager')
    app_window.show()

    sys.exit(app.exec_())
