#Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input("DIGITE UM NUMERO:"))
tot = 0
for p in range(1, n + 1):
    if n % p == 0:
        print("\033[34m", end=" ")
        tot += 1

    else:
        print("\033[31m", end=" ")
    print("{}".format(p), end=" ")

print("\n\033[mO nunero {} foi de visivel por {} numeros incluindo {}.".format( n, tot, n))
 
if tot <= 2:
    print("E um numero \033[34mPRIMO\033[m.")
else:
    print("\033[31mE por isso ele nao e um numero PRIMO\033[m.")
