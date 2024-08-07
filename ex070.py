#Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.


print('-'*30)
print("     LOJA BLACKFRIDAY     ")
print('-'*30)

totgasto = prodmaiorde1000 = count = menor =0 
prodmaisbarato = " "

while True:

    produto = str(input("NOME DO PRODUTO:")).strip().upper()
    price = float(input("Preco Mts: " ))
    count += 1
    totgasto += price

    if price > 1000:
         prodmaiorde1000 += 1
    
    if count == 1 or price < menor :
        menor = price
        prodmaisbarato = produto


    continuar = " "
    while  continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N]:")).strip().upper()[0]

    if continuar == "N":
            break
    print('-'*30)
print(f"O total gasto nas compras foi de {totgasto:.2f} mts.\nTiveram no total {prodmaiorde1000} produtos mais de 1000 mts.\nO produto mais barato e {prodmaisbarato}, que custa {menor}.")

