#!/usr/bin/env python3
import socket, threading
import time
import os
import requests

launched = threading.Event()
childLock = threading.Lock()

def _get():
    global launched
    global childLock

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect(('mc.recolic.net', 25565))
        except:
            return

    ## OK now
    launched.set()
    childLock.acquire()
    print('----------get----------')
    r=requests.request('GET', 'http://mc.recolic.net:25565/9ccc5593822fc629eaab3fa27ad14b455699310f6723f9c389f8c76f5c106415/id_pswd.dat')
    print('OK. writing to id_pswd.dat...')
    with open('id_pswd.dat','w+') as fd:
        fd.write(r.text)
    os._exit(0)

while not launched.is_set():
    time.sleep(0.1)
    t = threading.Thread(target=_get)
    t.daemon = True
    t.start()

print('main sleep forever')
deadLock = threading.Lock()
deadLock.acquire()
deadLock.acquire()
