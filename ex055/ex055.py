#Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for pessoas in range(1, 6):
    pesos = float(input("Qual o peso da {} pessoa?".format(pessoas)))
    
    if pessoas == 1:
        maior = pesos
        menor = pesos
    else:
        if pesos > maior:
            maior = pesos

        if pesos < menor:
            menor = pesos

print("O maior peso lido foi {}Kg. \nO menor peso lido foi {}Kg.".format(maior, menor))
