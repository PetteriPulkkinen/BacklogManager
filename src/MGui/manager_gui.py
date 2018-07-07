'''
Created by Petteri Pulkkinen
Date 6.6.2018

This file is used to contain graphical user interface components
for the application
'''

from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QTextEdit

class ManagerGUI(QMainWindow):
    def __init__(self):
        super(ManagerGUI,self).__init__()
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Backlog Manager")
        self.setCentralWidget(WidgetContainer())
        self.show()


class WidgetContainer(QWidget):
    def __init__(self):
        super(WidgetContainer,self).__init__()
        self._set_widgets()
        self._set_layout()

    def _set_widgets(self):
        self.proposed = StateWidget()
        self.started = StateWidget()
        self.done = StateWidget()

    def _set_layout(self):
        print("Set mgui widget layout")
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.proposed)
        self.hbox.addWidget(self.started)
        self.hbox.addWidget(self.done)
        self.setLayout(self.hbox)


class StateWidget(QWidget):
    def __init__(self):
        super(StateWidget,self).__init__()
        self._set_widgets()
        self._set_layout()

    def _set_widgets(self):
        self.textedit = QTextEdit()

    def _set_layout(self):
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.textedit)
        self.setLayout(self.vbox)
