# -*- coding: utf-8 -*-
# приклад клієнта, який виконує стохастичний пошук
import random, time
from tools import *

for i in range(100):
    x=random.uniform(-2, 2)
    y=send(x)
    if y=="Error": break
    print x, float(y)
    #time.sleep(random.random()) # тільки для тестування