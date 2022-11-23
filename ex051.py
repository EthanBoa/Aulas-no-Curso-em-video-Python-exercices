#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print ("=" * 100)
print ("                                   OS PRIMEROS 10 TERMOS DE UMA PA:                                     ")
print("=" * 100)

termo = int(input("PRIMEIRO TERMO:"))
razao = int(input("RAZAO:"))
PA = termo + (10 - 1) * razao
for c in range(termo, PA, razao):
    print("{}".format(c) ,end=" > ")
print(" ACABOU .")
