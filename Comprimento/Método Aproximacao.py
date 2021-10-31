
import numpy as np
from math import *

def expressao(t): # Expressão da Curva
    x, y = 6*cos(t) - 3*cos(6*t), 6*sin(t) - 3*sin(6*t)
    return x, y

n = 10_000 # Número de Pontos Usados
intervalo = np.arange(0, 2*pi, (2*pi)/n)

L = 0
for i in range(len(intervalo)-1):
    x1,y1 = expressao(intervalo[i]) # Primeiro Ponto
    x2,y2 = expressao(intervalo[i+1]) # Segundo Ponto
    deltaX = abs(x2-x1) # Delta X
    deltaY = abs(y2-y1) # Delta Y
    d = (deltaX**2 + deltaY**2)**0.5 # Distância entre os Dois Pontos
    L += d # Soma ao Comprimento da Curva

print(f"Comprimento Aproximado da Curva: {L}u")


