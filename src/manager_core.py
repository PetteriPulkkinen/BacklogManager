'''
    Created by Petteri Pulkkinen
    Date 6.6.2018

    This file is used to contain core functionalities for the application
'''

from enum import Enum
from datetime import datetime


class Backlog(object):
    '''
        Backlog is a container class for the tasks.
    '''
    def __init__(self):
        self.state_dict = {TaskState.PROPOSED : {}, TaskState.STARTED : {}, 
        TaskState.DONE : {}}

    def getTask(self, name):
        for key, task_dict in self.state_dict.items():
            if name in task_dict:
                return task_dict[name]
        return None

    def addTask(self, task):
        self.state_dict[task.state] = {task.name : task}
        print("Add task")

    def removeTask(self, name):
        for key, task_dict in self.state_dict:
            del task_dict[name]

    def printItems(self):
        for key, task_dict in self.state_dict.items():
            for key, task in task_dict.items():
                print(task)


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
        if self._start_date == None:
            self._start_date = datetime.now()
        self._done_date = datetime.now()

    def _dateString(self, date):
        s = str(date).split(' ')
        time = s[1][:8]
        return s[0] + ' ' + time

    def getState():
        return self.state

    def __str__(self):
        if self._done_date != None:
            return (self.name + " : " + str(self.state) + " started: "
            + self._dateString(self._start_date)
            + " Finished " + self._dateString(self._done_date))
        elif self._start_date != None:
            return (self.name + " : " + str(self.state) + " started: "
            + self._dateString(self._start_date))
        else:
            return (self.name + " : " + str(self.state) + " proposed: "
            + self._dateString(self._proposed_date))


class TaskState(Enum):
    PROPOSED = 0
    STARTED = 1
    DONE = 2
