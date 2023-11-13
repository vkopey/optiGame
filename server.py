# -*- coding: utf-8 -*-
import socket
import numpy as np

def f(x): #https://machinelearningmastery.com/1d-test-functions-for-function-optimization/
    return (x+1)**2 # функція
    #return np.sin(x) + np.sin((10.0 / 3.0) * x)

n=10 # максимальна кількість спроб
X=np.arange(-2, 2, 0.001)
Y=f(X)

i=Y.argmin()
argmin=X[i]
print "argmin=", argmin, "min=", Y[i]

import matplotlib.pyplot as plt
plt.plot(X,Y)
plt.scatter([argmin],[Y[i]],c='r')
plt.savefig("fig.png")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 50007))
s.listen(5)
C={} # містить дані: адреса клієнта : [список x, кількість спроб, мінімальне abs(x-argmin)]

while True:
    soc, addr = s.accept() # з'єднатись
    addr=addr[0]
    if not C.has_key(addr):
        C[addr]=[[], 0, None]
    x=soc.recv(255) # отримати
    try:
        x=float(x)
    except:
        x=None
    if x==None or C[addr][1]>n or x<min(X) or x>max(X): # якщо помилка
        soc.sendall("Error")
        soc.close()
        continue
    C[addr][0].append(x) # додати x
    C[addr][1]+=1 # збільшити кількість спроб
    y=f(float(x)) # значення f(x)
    soc.sendall(str(y)) # надіслати
    soc.close()
    for c in C: # для усіх клієнтів
        C[c][2]=min([abs(x-argmin) for x in C[c][0]]) # обчислити мінімальне абс. відхилення
    for c in sorted(C, key=lambda k: C[k][2]): # відсортувати клієнтів
        print c, C[c][1], C[c][2] # клієнт, спроба, мінімальне абс. відхилення
    print "___________________________"