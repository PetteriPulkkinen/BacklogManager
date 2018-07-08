'''
Created by Petteri Pulkkinen
Date 6.6.2018

This file is used to contain graphical user interface components
for the application
'''

from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QListWidget, QLabel, QListWidgetItem
import PyQt5.QtWidgets
from manager_core import Manager


class ManagerGUI(Manager, QMainWindow):
    def __init__(self):
        super(ManagerGUI,self).__init__()
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Backlog Manager")
        self.container = WidgetContainer()
        self.setCentralWidget(self.container)
        self.show()

    def update(self):
        states = self.backlog.get_all_states()


class WidgetContainer(QWidget):
    def __init__(self):
        super(WidgetContainer,self).__init__()
        self._set_widgets()
        self._set_layout()

    def _set_widgets(self):
        self.proposed = StateWidget("Proposed")
        self.started = StateWidget("Started")
        self.done = StateWidget("Done")

    def _set_layout(self):
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.proposed)
        self.hbox.addWidget(self.started)
        self.hbox.addWidget(self.done)
        self.setLayout(self.hbox)


class StateWidget(QWidget):
    def __init__(self, name):
        super(StateWidget,self).__init__()
        self.name = name
        self._set_widgets()
        self._set_layout()

    def _set_widgets(self):
        self.label = QLabel(self.name)
        self.items = QListWidget()
        item = QListWidgetItem("Item 1")

    def _set_layout(self):
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.items)
        self.setLayout(self.vbox)

class TaskWidget(QListWidgetItem):
    def __init__(self, name):
        super(TaskWidget, self).__init__()
