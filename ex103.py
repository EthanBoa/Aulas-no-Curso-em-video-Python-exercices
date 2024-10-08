#Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(jogador="Nome Desconhecido", golos =0):
    print("-="*30)
    print(f"O Jogador <{jogador}> marcou {golos}.")
    print("-="*30)


nome = str(input("Qual o nome do jogador? "))
gol = str(input("Quantos golos ele marcou? "))

if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == "":
    ficha(golos=gol)
else:
    ficha(nome,gol)

