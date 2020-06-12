# by checking expiry we can 

import threading
import os
import datetime


def check_expiry():
    global stop_thread
    # print("000")
    if start_date > expiry_date:
        print("Expired")
        stop_thread = True


def task1():
    print("ID of process running task 1: {}".format(os.getpid()))
    while True:
        if stop_thread:
            print("expires")
            break
        print("in while of task 1")


def task2():
    print("ID of process running task 2: {}".format(os.getpid()))
    while True:
        print("in while of task 2")


if __name__ == "__main__":
    # print ID of current process
    print("ID of process running main program: {}".format(os.getpid()))
    stop_thread = False
    # creating threads
    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')

    # starting threads
    t1.start()
    t2.start()
    start_date = datetime.date.today()
    # 30 june 2020 is expiry date
    expiry_date = datetime.date(2020, 6, 30)
