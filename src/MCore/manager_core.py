'''
    Created by Petteri Pulkkinen
    Date 6.6.2018

    This file is used to contain core functionalities for the application
'''

from enum import Enum
from datetime import datetime


class Manager(object):
    def __init__(self):
        self.backlog = Backlog()


class Backlog(object):
    '''
        Backlog is a container class for the tasks.
    '''
    def __init__(self):
        self.task_dict = {}

    def get_task(self, name):
        return self.task_dict[name]

    def add_task(self, task):
        self.task_dict[task.task_name] = task

    def remove_task(self, name):
        del self.task_dict[name]


class Task(object):
    '''
        Instance of task which are used to present one task in the backlog
    '''
    def __init__(self, name):
        self.task_name = name
        self._state = TaskStates.PROPOSED
        self._proposed_date = datetime.now()
        self._start_date = None
        self._done_date = None

    def _change_state(self, state, date):
        self._state = state
        date = datetime.now()

    def start_task(self):
        self._change_state(TaskStates.STARTED, self._start_date)

    def mark_task_done(self):
        self._change_state(TaskStates.DONE, self._done_dgit ate)

    def __str__(self):
        return self.task_name + ":" + str(self._state)


class TaskStates(Enum):
    PROPOSED = 0
    STARTED = 1
    DONE = 2
