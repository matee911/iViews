# coding: utf-8

from __future__ import print_function, division
import threading
import time
import random
import semaphore
import socket
import urllib2

def whatsmyip():
    req = urllib2.Request('http://ifconfig.me', None, {'User-Agent': 'curl/7.21.4'})
    return urllib2.urlopen(req).read()
whatsmyip = whatsmyip()

def slow_print(s):
    for c in s:
        print(c, end="")
        time.sleep(random.randint(1,5)/100)
    print()

def slow_socket(msg):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 7000))
    for c in msg:
        s.send(c)
        time.sleep(random.randint(5,9)/100)
    s.close()


class T(threading.Thread):
    def __init__(self, name, kwargs={}):
        super(T, self).__init__(name=name, kwargs=kwargs)
        self.kwargs = kwargs
        self.name = name

    def run(self):
        for i in range(10):
            self.kwargs['semaphore'].acquire(True)
            slow_socket("{} ThreadName:{} Count:{} ExternalIP:{}".format(time.time(), self.name, i, whatsmyip))
            self.kwargs['semaphore'].release()
            time.sleep(0.01)

def main():
    sem = threading.BoundedSemaphore(1)
    sem = semaphore.RedisSemaphore()
    for i in range(3):
        print(i)
        t = T(name='T{}'.format(i), kwargs=dict(semaphore=sem))
        t.start()


if __name__ == '__main__':
    main()
