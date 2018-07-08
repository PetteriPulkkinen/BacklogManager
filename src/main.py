'''
Created by Petteri Pulkkinen
Date 6.6.2018

This file is used to contain main funtion for program execution
'''

from manager_core import *

m = Manager()

def getUserInput():
    inp = input("Command: ").split(' ')
    cmd = inp[0]
    arg = ""
    try:
        arg1 = inp[1]
        arg2 = inp[2]
    except:
        pass
    if cmd == 'p':
        m.backlog.print_items()
    elif cmd == 'a':
        m.backlog.add_task(Task(arg1))
    elif cmd == 'c':
        if arg2 == '0':
            m.backlog.get_task(arg1).propose_task()
        if arg2 == '1':
            m.backlog.get_task(arg1).start_task()
        elif arg2 == '2':
            m.backlog.get_task(arg1).finish_task()
    elif cmd == 'd':
        m.backlog.remove_task(arg1)
    else:
        return 0

    return True

if __name__ == '__main__':
    '''
    app = QApplication(sys.argv)

    soft = Manager()

    sys.exit(app.exec_())
    '''
    task1 = Task("task1")
    task2 = Task("task2")
    task3 = Task("task3")
    task1.propose_task()
    task2.start_task()
    task3.finish_task()
    m.backlog.add_task(task1)
    m.backlog.add_task(task2)
    m.backlog.add_task(task3)
    while(getUserInput()):
        print("nice")

    exit(0)
