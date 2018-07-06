'''
    Created by Petteri Pulkkinen
    Date 6.6.2018

    This file is used to contain core functionalities for the application
'''

from enum import Enum
from datetime import datetime


class Manager(object):
    pass


class Backlog(object):
    pass


class Task(object):
    '''
        Instance of task which are used to present one task in the backlog
    '''
    def __init__(self, name):
        self._task_name = name
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
        self._change_state(TaskStates.DONE, self._done_date)


class TaskStates(Enum):
    PROPOSED = 0
    STARTED = 1
    DONE = 2
