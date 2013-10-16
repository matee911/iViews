# coding: utf-8

"""
Prepares semaphore counter and receives slowly send data
from workers (distributed threads).
Received data is printed on stdout.
"""

import redis
import socket

#: Number of connections/counter value
LIMIT = 1

def prepare():
    """Prepares counter"""
    r = redis.StrictRedis()
    r.delete('sem')
    for _ in range(LIMIT):
        r.lpush('sem', 1)
    print "Semaphore counter is set to: %s" % r.llen('sem')

def recv(sckt):
    """Reads in loop data from client,
    because it is send slowly (there is a sleep between each character)"""
    data = ""
    while True:
        r = sckt.recv(2)
        if len(r) == 0:
            return data.replace('\n', '')
        else:
            data += r

def run_server():
    """Starts server and waits for connection from worker"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 7000))
    s.listen(LIMIT)
    while True:
        client, _ = s.accept()
        data = recv(client)
        print data
        client.close()


def main():
    prepare()
    run_server()

if __name__ == '__main__':
    main()

