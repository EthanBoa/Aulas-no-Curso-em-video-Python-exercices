# Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
a = input("Qual o nome da primeiro aluno:")
b = input("Qual o nome da segundo aluno:")
c = input("Qual o nome da terceiro aluno:")
d = input("Qual o nome da querto aluno:")
l = [a, b, c, d]
e = choice(l)
print("O ecolhido e {}".format(e))
