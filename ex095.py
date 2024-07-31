#Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogado

dic = {}
golos= []
s = []
time = []
count = 0

while True:
    # Criando as variáveis do dicionário
    dic.clear()
    dic["nome"] = str(input("Qual o nome do jogador: "))
    dic["partidas"] = int(input("Quantas partidas ele jogou: "))
    golos.clear()
    # Fazendo um loop finito para saber quantos gols o jogador marcou em cada partida feita 
    for i in range(0, dic["partidas"]):
        golos.append(int(input(f"Quantos gols ele marcou na partida {i+1}: ")))
    
    # Fazendo clone da lista golos no dicionário dic
    dic["golos"] = golos[:]
    
    # Criando um dicionário que conte quantos gols o jogador fez em todas as partidas   
    dic["total"] = sum(golos)
    time.append(dic.copy())
    count += 1
    while True:
        # Criando a finalização do loop
        resposta = str(input("Quer continuar? [S/N]")).strip().upper()[0]
        if resposta in "SN":
            break
    if resposta == "N":
        break

# Mostrando as saídas

print("-="*40)
print("Cod   Nome                Gols                  Total")
print("-"*80)
for k, v in enumerate(time):
    print(f"{k:<5} {v['nome']:<20} {str(v['golos']):<20} {v['total']:<5}")

print("-="*40)

dados = str(input("Qual jogar vc quer ver os dados? (000 para parar) "))

if dados == time[dados]:
    print(time[dados])

