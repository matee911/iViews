# coding: utf-8

import threading
import redis
import socket

LIMIT = 1

def prepare():
    r = redis.StrictRedis()
    print r.llen('sem')
    r.delete('sem')
    for i in range(LIMIT):
        r.lpush('sem', 1)
    print r.lrange('sem', 0, r.llen('sem'))

def recv(sckt):
    data = ""
    while True:
        r = sckt.recv(2)
        if len(r) == 0:
            return data.replace('\n', '')
        else:
            data += r

def run_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 7000))
    s.listen(LIMIT)
    while True:
        client, addr = s.accept()
        
        data = recv(client)
        print data
        client.close()


def main():
    prepare()
    run_server()

if __name__ == '__main__':
    main()

