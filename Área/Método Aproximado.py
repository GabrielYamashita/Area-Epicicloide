
import numpy as np
from math import *

def expressao(t): # Expressão da Curva
    x, y = 6*cos(t) - 3*cos(6*t), 6*sin(t) - 3*sin(6*t)
    return x, y

def distancia(x1,y1,x2,y2): # Calcular a Distância entre dois pontos
    deltaX = abs(x2-x1)
    deltaY = abs(y2-y1)
    d = (deltaX**2 + deltaY**2)**0.5
    return d

n = 1_000_000 # Número de Triângulos Usados
intervalo = np.arange(1.64, 2.13, (2.13)/n) # Intervalo usado Para Calcular a Área

A = 0
for i in range(len(intervalo)-1):
    x1,y1 = expressao(intervalo[i]) # Primeiro Ponto do Triângulo
    x2,y2 = expressao(intervalo[i+1]) # Segundo Ponto do Triângulo
    a = distancia(0,0,x1,y1) # Lado A do Triângulo
    b = distancia(0,0,x2,y2) # Lado B do Triângulo
    c = distancia(x1,y1,x2,y2) # Lado C do Triângulo
    p = (a+b+c)/2 # Formula de Herão (p)
    A += (p*(p-a)*(p-b)*(p-c))**0.5 # Formula de Herão (fórmula)

print(f"Área Aproximado da Curva: {5*A}") # Multiplica por 5 porque a Curva é simétrica


