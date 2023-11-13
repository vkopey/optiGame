# -*- coding: utf-8 -*-
import socket
def send(x):
    u"Надсилає дані x на сервер. Поверає отримані від сервера дані."
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 50007))
    s.sendall(str(x))
    y=s.recv(255)
    s.close()
    return y