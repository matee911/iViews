# coding: utf-8

import threading
import redis
import time
# http://hg.python.org/cpython/file/2.7/Lib/threading.py

class RedisSemaphore(threading._Semaphore):
    def __init__(self):
        self.r = redis.StrictRedis()
        self.cond = threading.Condition()

    def acquire(self, blocking=True):
        rc = False
        while self.r.rpop('sem') == None:
            if not blocking:
                break
            time.sleep(0.0005)
        else:
            rc = True
        return rc

    __enter__ = acquire # with statement compatible

    def release(self):
        self.r.rpush('sem', 1)

    def __exit__(self, t, v, tb):
        self.release()

if __name__ == '__main__':
    s = RedisSemaphore()
    s.acquire()

