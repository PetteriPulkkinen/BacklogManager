'''
Created by Petteri Pulkkinen
Date 6.6.2018

This file is used to contain graphical user interface components
for the application
'''

from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QListWidget, QLabel, QListWidgetItem, QPushButton
from PyQt5.QtWidgets import QInputDialog
from manager_core import Backlog, Task, TaskState


class ManagerGUI(QMainWindow):
    def __init__(self):
        super(ManagerGUI, self).__init__()
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Backlog Manager')
        self.central_widget = CentralWidget()
        self.setCentralWidget(self.central_widget)
        self.show()


class CentralWidget(QWidget):
    def __init__(self):
        super(CentralWidget, self).__init__()
        self.left_button = QPushButton('Left')
        self.remove_button = QPushButton('Remove')
        self.add_button = QPushButton('Add')
        self.right_button = QPushButton('Right')
        self.left_button.clicked.connect(self._leftButtonClicked)
        self.remove_button.clicked.connect(self._removeButtonClicked)
        self.add_button.clicked.connect(self._addButtonClicked)
        self.right_button.clicked.connect(self._rightButtonClicked)
        self.backlog_widget = BacklogWidget()
        self._initLayout()

    def _initLayout(self):
        label_hbox = QHBoxLayout()
        label_hbox.addWidget(QLabel('Proposed'))
        label_hbox.addWidget(QLabel('Started'))
        label_hbox.addWidget(QLabel('Done'))
        label_widget = QWidget()
        label_widget.setLayout(label_hbox)

        button_hbox = QHBoxLayout()
        button_hbox.addWidget(self.left_button)
        button_hbox.addWidget(self.remove_button)
        button_hbox.addWidget(self.add_button)
        button_hbox.addWidget(self.right_button)
        button_widget = QWidget()
        button_widget.setLayout(button_hbox)

        widget_layout = QVBoxLayout()
        widget_layout.addWidget(label_widget)
        widget_layout.addWidget(self.backlog_widget)
        widget_layout.addWidget(button_widget)

        self.setLayout(widget_layout)

    def _leftButtonClicked(self):
        task = self.backlog_widget.getActiveTask()
        self.backlog_widget.changeTaskState(task, -1)

    def _rightButtonClicked(self):
        task = self.backlog_widget.getActiveTask()
        self.backlog_widget.changeTaskState(task, 1)

    def _addButtonClicked(self):
        text, ok = QInputDialog.getText(self, 'Input task name', 'Add task')
        if ok:
            print('Add task with name: {}'.format(text))
            self.backlog_widget.addTaskWidget(TaskWidget(text))
        else:
            print('Task not added!')

    def _removeButtonClicked(self):
        task = self.backlog_widget.getActiveTask()
        print('Remove button clicked for task: {}'.format(task.name))
        self.backlog_widget.removeTaskWidget(task)


class BacklogWidget(QWidget, Backlog):
    def __init__(self):
        super(BacklogWidget, self).__init__()
        t2 = TaskWidget('task2')
        t2._finishTask()
        self.addTask(TaskWidget('task1'))
        self.addTask(t2)
        self.addTask(TaskWidget('task3'))
        self.state_widgets = []
        self._current_state_activated = None
        self._initStateWidgets()
        self._initTaskWidgets()

    def addTaskWidget(self, task):
        self.addTask(task)
        sw = self._getStateWidget(task.state)
        sw.addItem(task)

    def changeTaskState(self, task, direction):
        self.removeTaskWidget(task)
        task.changeState(TaskState(task.state.value + direction))
        self.addTaskWidget(task)
        print(self.printTasks())

    def removeTaskWidget(self, task):
        sw = self._getStateWidget(task.state)
        row = sw.currentRow()
        sw.takeItem(row)
        self.removeTask(task.name)

    def getActiveTask(self):
        sw = self._getStateWidget(self._current_state_activated)
        return sw.currentItem()

    def _initStateWidgets(self):
        self.hbox = QHBoxLayout()
        for state in list(TaskState):
            sw = StateWidget(state)
            self.hbox.addWidget(sw)
            sw.itemClicked.connect(self._itemClicked)
            self.state_widgets.append(sw)
        self.setLayout(self.hbox)

    def _initTaskWidgets(self):
        for task in self.task_list:
            self._getStateWidget(task.state).addItem(task)

    def _getStateWidget(self, state):
        for widget in self.state_widgets:
            if widget.state is state:
                return widget
        return None

    def _itemClicked(self, item):
        print("Clicked: {}".format(item.name))
        sw = self._getStateWidget(item.state)
        self._current_state_activated = item.state
        sw.setCurrentItem(item)


class StateWidget(QListWidget):
    def __init__(self, state):
        super(StateWidget, self).__init__()
        self.state = state


class TaskWidget(Task, QListWidgetItem):
    def __init__(self, name):
        QListWidgetItem.__init__(self, name)
        Task.__init__(self, name)
        print('TaskWidget')
