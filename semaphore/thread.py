# coding: utf-8

from __future__ import print_function, division
import threading
import time
import random
import semaphore
import socket
import urllib2
import const

def whatsmyip():
    req = urllib2.Request('http://ifconfig.me', None,
            {'User-Agent': 'curl/7.21.4'})
    return urllib2.urlopen(req).read()
WHATS_MY_IP = whatsmyip()

def slow_socket(msg):
    sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sck.connect((const.MASTER_HOST, 7000))
    for c in msg:
        sck.send(c)
        time.sleep(random.randint(5, 9)/100)
    sck.close()


class Thread(threading.Thread):
    def __init__(self, name, kwargs={}):
        super(Thread, self).__init__(name=name, kwargs=kwargs)
        self.kwargs = kwargs
        self.name = name

    def run(self):
        for i in range(10):
            self.kwargs['semaphore'].acquire(True)
            slow_socket("{} ThreadName:{} Count:{} ExternalIP:{}".format(
                time.time(), self.name, i, WHATS_MY_IP))
            self.kwargs['semaphore'].release()
            time.sleep(0.01)

def main():
    sem = semaphore.DistributedSemaphore()
    for i in range(3):
        print(i)
        thread = Thread(name='T{}'.format(i), kwargs=dict(semaphore=sem))
        thread.start()


if __name__ == '__main__':
    main()
