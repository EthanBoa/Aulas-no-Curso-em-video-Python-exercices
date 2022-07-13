#  Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import hypot
ca =float(input("Qual e o valor do cateto adjacente:"))
co = float(input("Qual e o valor do cateto oposto:"))
h = hypot(ca, co)
print("O valor da hipotenusa e: {}".format(h))
