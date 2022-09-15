# Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
c = randint(0, 5)
n = str(input(" Adivinhe em que numero estou pensando de  0 - 5. Sera que vc consegue acertar?  "))
if c == n:
    print("Processando...")
    print("vc acertou parabens!")
else:
    print('Vc falhou o numero que eu escolhe foi {}!Tente de novo'.format(c))