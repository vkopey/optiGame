# -*- coding: utf-8 -*-
# приклад клієнта, який виконує стохастичний пошук
import random, time
from tools_http import *

for i in range(10):
    x=random.uniform(-2, 2)
    y=send(x)
    if y=="Error": break
    print(x, float(y))
    time.sleep(1)
    #time.sleep(random.random()) # тільки для тестування