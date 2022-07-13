# Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc
n = float(input("Digite um numero:"))
i = trunc(n)
print("O numero {} tem parte inteira {}".format(n, i))
