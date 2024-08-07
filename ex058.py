#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
random = randint(0, 10)
print("""Sou o seu computador...
Acabei de pensar em um numero de 0 - 10!
""")
palpites = 0
acertou = False

while not acertou:
    palyer = int(input("Qual o seu palpite?"))
    palpites += 1
    if random == palyer:
        acertou = True

    else:
        if palyer < random:
            print("Um bacadinho mais...! Tente novamente:")
        
        elif palyer > random:
            print("Tente com um numero menor....! Tente novamente:")
            
print("Venceu com {} tentativas!".format(palpites))