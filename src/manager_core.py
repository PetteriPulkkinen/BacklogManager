'''
    Created by Petteri Pulkkinen
    Date 6.6.2018

    This file is used to contain core functionalities for the application
'''

from enum import Enum
from datetime import datetime
import pprint


class Backlog(object):
    '''
        Backlog is a container class for the tasks.
    '''
    def __init__(self):
        self.task_list = []

    def getTask(self, name):
        for task in self.task_list:
            if task.name == name:
                return task
        return None

    def addTask(self, task):
        self.task_list.append(task)

    def removeTask(self, name):
        task = self.getTask(name)
        self.task_list.remove(task)

    def printTasks(self):
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.task_list)


class Task(object):
    '''
        Instance of task which are used to present one task in the backlog
    '''
    def __init__(self, name):
        self.name = name
        self.state = TaskState.PROPOSED
        self._proposed_date = datetime.now()
        self._start_date = None
        self._done_date = None

    def proposeTask(self):
        self.state = TaskState.PROPOSED
        self._proposed_date = datetime.now()
        self._start_date = None
        self._done_date = None

    def startTask(self):
        self.state = TaskState.STARTED
        self._start_date = datetime.now()
        self._done_date = None

    def finishTask(self):
        self.state = TaskState.DONE
        if self._start_date is None:
            self._start_date = datetime.now()
        self._done_date = datetime.now()

    def _dateString(self, date):
        s = str(date).split(' ')
        time = s[1][:8]
        return s[0] + ' ' + time

    def __str__(self):
        if self._done_date is not None:
            return (self.name + " : " + str(self.state) + " started: "
                    + self._dateString(self._start_date)
                                + " Finished " + self._dateString(self._done_date))
        elif self._start_date is not None:
            return (self.name + " : " + str(self.state) + " started: "
                    + self._dateString(self._start_date))
        else:
            return (self.name + " : " + str(self.state) + " proposed: "
                    + self._dateString(self._proposed_date))


class TaskState(Enum):
    PROPOSED = 0
    STARTED = 1
    DONE = 2
