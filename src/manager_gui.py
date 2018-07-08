'''
Created by Petteri Pulkkinen
Date 6.6.2018

This file is used to contain graphical user interface components
for the application
'''

from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QListWidget, QLabel, QListWidgetItem
import PyQt5.QtWidgets
from manager_core import *


class ManagerGUI(QMainWindow):
    def __init__(self):
        super(ManagerGUI, self).__init__()
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Backlog Manager")
        self.bl_widget = BacklogWidget()
        self.bl_widget.init()
        self.setCentralWidget(self.bl_widget)
        self.show()


class BacklogWidget(QWidget, Backlog):
    def __init__(self):
        super(BacklogWidget, self).__init__()

        self.addTask(Task("task1"))
        self.addTask(Task("task2"))
        self.addTask(Task("task3"))
        self.getTask("task3").startTask()

        self.state_widgets = {}

    def init(self):
        self._initListWidgets()
        self._initTaskWidgets()

    def _initListWidgets(self):
        self.hbox = QHBoxLayout()
        for state in self.state_dict:
            self.state_widgets[state] = StateWidget()
            self.hbox.addWidget(self.state_widgets[state])
        self.setLayout(self.hbox)

    def _initTaskWidgets(self):
        for state, task_dict in self.state_dict.items():
            for name in task_dict.keys():
                self.state_widgets[state].task_list.addItem(TaskWidget(name))



class StateWidget(QWidget):
    def __init__(self):
        super(StateWidget, self).__init__()
        self.vbox = QVBoxLayout()
        self.task_list = QListWidget()
        self.label = QLabel("Label")
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.task_list)
        self.setLayout(self.vbox)


class TaskWidget(QListWidgetItem):
    def __init__(self, name):
        super(TaskWidget, self).__init__(name)
        self.name = name
