'''
    Created by Petteri Pulkkinen
    Date 6.6.2018

    This file is used to contain core functionalities for the application
'''

from enum import Enum
from datetime import datetime

class Manager(object):
    def __init__(self):
        super(Manager,self).__init__()
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

    def print_items(self):
        for i in self.task_dict.items():
            print(i[1])

    def get_all_states(self):
        states = {}
        for item in task_dict.items():
            states[item[0]] = item[1].get_state()

        return states



class Task(object):
    '''
        Instance of task which are used to present one task in the backlog
    '''
    def __init__(self, name):
        self.task_name = name
        self._state = TaskState.PROPOSED
        self._proposed_date = datetime.now()
        self._start_date = None
        self._done_date = None

    def propose_task(self):
        self._state = TaskState.PROPOSED
        self._proposed_date = datetime.now()
        self._start_date = None
        self._done_date = None

    def start_task(self):
        self._state = TaskState.STARTED
        self._start_date = datetime.now()
        self._done_date = None

    def finish_task(self):
        self._state = TaskState.DONE
        if self._start_date == None:
            self._start_date = datetime.now()
        self._done_date = datetime.now()

    def _date_string(self, date):
        s = str(date).split(' ')
        time = s[1][:8]
        return s[0] + ' ' + time

    def get_state():
        return self._state

    def __str__(self):
        if self._done_date != None:
            return (self.task_name + " : " + str(self._state) + " started: "
            + self._date_string(self._start_date)
            + " Finished " + self._date_string(self._done_date))
        elif self._start_date != None:
            return (self.task_name + " : " + str(self._state) + " started: "
            + self._date_string(self._start_date))
        else:
            return (self.task_name + " : " + str(self._state) + " proposed: "
            + self._date_string(self._proposed_date))


class TaskState(Enum):
    PROPOSED = 0
    STARTED = 1
    DONE = 2
