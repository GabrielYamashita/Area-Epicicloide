
import numpy as np
from math import *

import matplotlib.pyplot as plt


def x_linha(t):
    x = -6*sin(t)+18*sin(6*t)
    return x

def y_linha(t):
    y = 6*cos(t)-18*cos(6*t)
    return y

n = 10_000
intervalo = np.arange(0, 2*pi, 2*pi/n)

tx, ty = [], []
for i in intervalo:
    tx.append(x_linha(i))
    ty.append(y_linha(i))

dicx = dict(zip(intervalo, tx))
dicy = dict(zip(intervalo, ty))

c = 0
tx = []
for k1,v1 in dicx.items():
    if v1 < 0.032 and v1 > -0.032:
        c+=1
        print(f"x{c}: {v1}")
        tx.append(k1)

print("")

c = 0
ty = []
for k2,v2 in dicy.items():
    if v2 < 0.032 and v2 > -0.032:
        c+=1
        print(f"y{c}: {v2}")
        ty.append(k2)
    
print(f"\ntx:{tx}")
print(f"ty:{ty}")

