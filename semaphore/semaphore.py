# coding: utf-8

"""
Module contains distributed semaphore implementation,
which needs to work redis server (as it acts as master counter).
It doesn't implement standard semaphore API, because then in each
worker could be initialized with different value.
"""

import threading
import time
import redis
import const

# pylint: disable=R0924,W0212
class DistributedSemaphore(threading._Semaphore):
    """Distributed semaphore class
    which uses redis as a master state controller"""
    def __init__(self):
        super(DistributedSemaphore, self).__init__(self)
        self.redis = redis.StrictRedis(host=const.REDIS_HOST)

    def acquire(self, blocking=True):
        acquired = False
        while self.redis.rpop('sem') == None:
            if not blocking:
                break
            time.sleep(0.0005)
        else:
            acquired = True
        return acquired

    __enter__ = acquire # with statement compatible

    def release(self):
        self.redis.rpush('sem', 1)

    def __exit__(self, t, v, tb):
        self.release()

