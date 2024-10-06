#Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep


def sortear(lista):
    print("SORTEANDO OS 5 NUMEROS DA LISTA:", end= " ")
    for num in range(0,5):
        n= randint(0,10)
        lista.append(n)
        print(f"{n}", end=" ", flush=True)
        sleep(0.3)
    print("Feito!")
def somar(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma+=numero
    print(f"A soma dos numeros pares da lista {num} da {soma}")

num =[]
sortear(num)
somar(num)