
import numpy as np
from math import *


def expressao(t): # Expressões Usadas
   # resultado = sqrt(360+216*cos(5*t)) # Comprimento
   resultado = 18*(-2*pow(sin(t),2) + 7*sin(t)*sin(6*t) - 3*pow(sin(6*t),2)) # Área
   return resultado

def metodoTrapezios(ti, tf, n):
   passo = (tf - ti)/n
   x = np.arange(ti, tf+passo, passo) # Os intervalos da Expressão (t)
   fx = []
   for i in x:
      fx.append(expressao(i)) # Valores de f(t)

   soma = sum(fx)-fx[0]-fx[len(fx)-1] # Soma dos Pontos Intermediários

   calculo = passo/2 * (fx[0] + 2*soma + fx[len(fx)-1]) # Formula do Método dos Trapézios

   return calculo

def erro(tf, ti, erroMax, dMax): # Calcula a Área Máxima de Erro e retorna quantidade de Trapézios
   n = sqrt(abs((dMax * (tf-ti)**3) / (12*erroMax)))
   return ceil(n)

ti = 0 # Limite de Integração Inicial
tf = 2*pi # Limite de Integração Final
erroMax = [0.1] # Erros a serem Usados
dMaxC = 225 # Valor Máximo da Derivada Segunda da Expressão do Comprimento
dMaxA = 700.4 # Valor Máximo da Derivada Segunda da Expressão do Área
tipo = input('Qual tipo de Cálculo: ') # Seleciona se é Cálculo da Área(A) ou do Comprimento(C)

for i in range(len(erroMax)):
   if tipo.lower() in ['a', 'area', 'área']:
      n = erro(1.64,2.13,erroMax[i],dMaxC)
      print(f"Erro: {erroMax[i]}u\u00b2")
      print(f"n: {n} trapézios")
      print(f"Área Aproximada: {5*(abs(metodoTrapezios(1.64, 2.13, n))):.2f}u\u00b2\n")

   elif tipo.lower() in ['c', 'comprimento']:
      n = erro(ti,tf,erroMax[i],dMaxA)
      print(f"Erro: {erroMax[i]}u")
      print(f"n: {n} trapézios")
      print(f"Comprimento Aproximado: {abs(metodoTrapezios(ti, tf, n)):.2f}u\n")

