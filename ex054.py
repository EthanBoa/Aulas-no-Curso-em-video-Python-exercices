#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
actual = date.today().year
totmaior = 0
totmenor = 0

for pessoas in range(1,8):
    nascimento = int(input("Em que ano a {} pessoa nasceu?".format(pessoas)))
    idade = actual - nascimento

    if idade < 21:
        totmenor += 1 
    else:
       totmaior += 1
print("Ao todo tivemos {} pessoas maiores de idade \nE {} pessoas menores de idade. ".format(totmaior, totmenor))
    
