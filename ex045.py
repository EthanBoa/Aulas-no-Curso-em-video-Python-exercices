#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

itens = ("PEDRA " , "PAPEL", "TISOURA")

computador = randint(0, 2)

print('''Suas opçoes:

[ 0 ]  PEDRA

[ 1 ]  PAPEL

[ 2 ]  TISOURA

''')

Jogador = int(input("QUAL JOGADA VC VAI FAZER?"))

print("_-" * 30)
print(" O computador jogou {}".format(itens[computador]))
print(" O Jogador jogou {}".format(itens[Jogador]))
print("_-" * 30)

sleep(0.5)
print("JO") 

sleep(1)
print("KEM")

sleep(1)
print("PO")

print("_-" * 20)

if computador == 0: #COMPUTADOR ESCOLHEU PEDRA
    if Jogador == 0: 
        print(" EMPATE")
    
    elif Jogador == 1:
        print("VOCE GANHOU")

    elif Jogador == 2:
        print("VOCE PERDEU")
    
    else:
        print("Jogada invalida jogue de novamente.")
    
elif computador == 1:  #COMPUTADOR ESCOLHEU PAPEL
     if Jogador == 0: 
        print(" VOCE GANHO ")
    
     elif Jogador == 1:
        print(" EMPATE")

     elif Jogador == 2:
        print(" VOCE PERDEU ")

     else:
        print( "Jogada invalida jogue de novamente .")

elif computador == 2:  #COMPUTADOR ESCOLHEU TESOURA
    if Jogador == 0: 
        print(" VOCE PERDEU ")
    
    elif Jogador == 1:
        print(" VOCE GANHOU ")

    elif Jogador == 2:
        print(" EMPATE ")

else:
    print(" JOGADA INVALIDA \n TENTE NOVAMENTE")
