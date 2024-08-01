#Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
from time import sleep
def area(c, l):
    a =  c*l
    print(f"A area sera dada por {a}m2")

def sep():
    print("="*60)


sep()
sleep(1)
print("                 CALCULO DA AREA")
sleep(1)
sep()
c = float(input("Digite o valor do comprimento: "))
l = float(input("Digite o valor da largura: "))

sep()
sleep(1)
print(f"Para o comprimento temos {c}m e a largura temos {l}m.")
sleep(1)
print("calculando.....")
sep()
sleep(2)
area(c,l)
