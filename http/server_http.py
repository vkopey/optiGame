# -*- coding: utf-8 -*-
from bottle import get, run, request
import numpy as np

def f(x): #https://machinelearningmastery.com/1d-test-functions-for-function-optimization/
    return (x+1)**2 # функція
    #return np.sin(x) + np.sin((10.0 / 3.0) * x)

n=10 # максимальна кількість спроб
X=np.arange(-2, 2, 0.001)
Y=f(X)

i=Y.argmin()
argmin=X[i]
print("argmin=", argmin, "min=", Y[i])

import matplotlib.pyplot as plt
plt.plot(X,Y)
plt.scatter([argmin],[Y[i]],c='r')
plt.savefig("fig.png")

C={} # містить дані: адреса клієнта : [список x, кількість спроб, мінімальне abs(x-argmin)]

@get('/search') # http://localhost:8080/search?x=0.5
def search():
    global n, argmin
    addr=request.remote_addr
    if C.get(addr)==None:
        C[addr]=[[], 0, None]
    x = request.query.get('x')
    try:
        x=float(x)
    except:
        x=None
    if x==None or C[addr][1]>n or x<min(X) or x>max(X): # якщо помилка
        return "Error"
    C[addr][0].append(x) # додати x
    C[addr][1]+=1 # збільшити кількість спроб
    y=f(float(x)) # значення f(x)

    for c in C: # для усіх клієнтів
        C[c][2]=min([abs(x-argmin) for x in C[c][0]]) # обчислити мінімальне абс. відхилення
    for c in sorted(C, key=lambda k: C[k][2]): # відсортувати клієнтів
        print(c, C[c][1], C[c][2]) # клієнт, спроба, мінімальне абс. відхилення
    print("___________________________")
    return str(y) # надіслати


run(host='localhost', port=8080)