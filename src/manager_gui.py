'''
Created by Petteri Pulkkinen
Date 6.6.2018

This file is used to contain graphical user interface components
for the application
'''

from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QListWidget, QLabel, QListWidgetItem
from manager_core import Backlog, Task, TaskState


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
        self.t1 = TaskWidget("task1")
        self.t2 = TaskWidget("task2")
        self.t3 = TaskWidget("task3")
        self.addTask(self.t1)
        self.addTask(self.t2)
        self.addTask(self.t3)
        self.state_widgets = []

    def init(self):
        self._initStateWidgets()
        self._initTaskWidgets()

    def _initStateWidgets(self):
        self.hbox = QHBoxLayout()
        for state in list(TaskState):
            sw = StateWidget(state)
            self.hbox.addWidget(sw)
            self.state_widgets.append(sw)
        self.setLayout(self.hbox)

    def _initTaskWidgets(self):
        for task in self.task_list:
            self.getStateWidget(task.state).task_list.addItem(task)

    def getStateWidget(self, state):
        for widget in self.state_widgets:
            if widget.state is state:
                return widget
        return None


class StateWidget(QWidget):
    def __init__(self, state):
        super(StateWidget, self).__init__()
        self.vbox = QVBoxLayout()
        self.task_list = QListWidget()
        self.label = QLabel("Label")
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.task_list)
        self.setLayout(self.vbox)
        self.state = state


class TaskWidget(Task, QListWidgetItem):
    def __init__(self, name):
        QListWidgetItem.__init__(self, name)
        Task.__init__(self, name)
        print("TaskWidget")
