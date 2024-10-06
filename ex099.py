#Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def maior(*n):
    count=maior=0
    print(f"Analizando os valores...")

    for value in n:
        print(value, end=" ", flush=True)
        sleep(0.3)
        if count == 0:
            maior = value
        else:
            if maior<value:
                maior=value
        count+=1
    print(f"Foram adicionados {count} valores ao todo.\nO maior valor adicionado foi {maior}")


#Programa principal
maior(2,3,4,5,6)