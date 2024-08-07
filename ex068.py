#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

print("=-" * 51)
print("                                      \033[36m VAMOS JOGAR IMPAR PAR? \033[m                          ")
print("=-" * 51)

wins = 0

while True:
    user = int(input("Digite um numero:"))
    computador  = randint(0,10)
    soma = user + computador
    escolha = " "

    while escolha not in "PI":
        escolha = str(input("PAR ou IMPAR [P/I]")).strip().upper()[0]
    
    print(f"O jogador escolheu {user} e o computador {computador}. Total de {soma} ", end =" " )
    print("DEU PAR" if soma % 2 == 0 else "IMPAR")
    
    if escolha == "P":
        if soma % 2 == 0:
            print("Vc venceu.")
            wins +=1
        
        else:
            print("Vc perdeu")
            break

    elif escolha == "I":
        if soma % 2 != 0:
            print("Vc ganhou.")
            wins +=1

        else:
            print("Vc perdeu")
            break

    else:
        break

    print("Let's play again...")
print(f"GAME OVER..! Vc ganhou {wins}.")