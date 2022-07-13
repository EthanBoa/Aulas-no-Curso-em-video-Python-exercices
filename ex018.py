#Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
from math import radians, sin, cos, tan
a = float(input("Qual e o valor do angulo:"))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print("O valor do seno e {:.2f} \n O valor do cosseno e {:.2f}\n  O valor da tangente e {:.2f}".format(s, c, t))
