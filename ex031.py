#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
d = float(input("QUal e a distancia da sua viajem?"))
print("Vc vai comecar uma viagem de \033[4;33m{}km\033[m.".format(d))
if d <= 200:
    print("O cuto da sua viagem e de \033[4;33m{}mts\033[m.".format(d * 0.50))
else:
    print("O custo da sua viagem e de \033[4;33m{}mts\033[m.".format(d * 0.45))