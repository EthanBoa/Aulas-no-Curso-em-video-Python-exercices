#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

#criando dicionario e lista
dic = {}
golos = []

#criando as variaveis do dicionario
dic["nome"] = str(input("Qual o nome do jogador: "))
dic["partidas"] = int(input("Quantas partidas ele jogou: "))

#fazendo um loop finito para saber quantos golos o jogado marcou em cada partida feita 
for i in range(0, dic["partidas"]):
    golos.append(int(input(f"Quantos golos ele marcou na partida {i+1}: ")))
 
#Fazendo clone da lista golos no dicionario dic
dic["golos"] = golos[:]
 
#crindo um dicionario que conte quantos golos o jogador fez em todas as partidas   
dic["total"]= sum(golos)

#Mostrando as saidas
print("-="*40)
print(dic)

print("-="*40)
print(f"No campo noem tem o valor {dic['nome']}.\nNo campo partidas tem o valor {dic['partidas']}.\nNo campo golos tem o valor {dic['golos']}.\nNo campo total tem o valor {dic['total']}.")

print("-="*40)

print(f"O jogador {dic['nome']} jogou {dic["partidas"]} partidas.")
for i, v in enumerate(dic["golos"]):
    print(f"      ==> Na partida {i}, marcou {v} golos.")
print(f"Foi um total de  {dic['total']}")