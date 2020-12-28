# -*- coding: utf-8 -*-
# 使用 Threading 模块创建线程，直接从 threading.Thread 继承，然后重写__init__ 和 run方法

import threading
import time


class myThread(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):  # 把要执行的代码写到 run 函数里面，线程在创建后会直接运行 run 函数
        print("Starting %s" % self.name)
        print_time(self.name, self.counter, 5)
        print("Exiting %s" % self.name)


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启线程
thread1.start()
thread2.start()

print("Exiting Main Thread")
