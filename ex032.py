#Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
a = int(input("Que ano quer analisar? Coloque 0 pra analisar o ano actual:"))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print("O ano e \033[4;36;47mBissesto!\033[m")
else:
    print("O ano  \033[4;36;47mNao e bissesto!\033[m] ")