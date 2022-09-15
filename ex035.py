#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
a = float(input("Primeiro lado:"))
b = float(input("Segundo lado:"))
c = float(input("Terceiro lado:"))
from time import sleep
print("\033[43m+=\033[m"*30)

print("\033[35mAnalizando os dados...\033[m")
sleep(5)
 
print("\033[43m+=\033[m"*30)

if ( a + b >= c and b + c >= a and a + c >= b ):
    print("\033[44mEsse dados podem formar um triangulo.\033[m")
else:
    print("\033[41mEsse dados nao podem formar um triangulo.\033[m")