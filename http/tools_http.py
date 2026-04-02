# -*- coding: utf-8 -*-
import urllib.request

def send(x):
    "Надсилає дані x на сервер. Поверає отримані від сервера дані."
    with urllib.request.urlopen('http://localhost/search?x='+str(x)) as response:
        html = response.read() #(returns bytes)
        html=html.decode('utf-8')
    return html
