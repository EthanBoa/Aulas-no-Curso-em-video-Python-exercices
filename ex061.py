#Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print ("=" * 100)
print ("                                    TERMOS DE UMA PA:                                     ")
print("=" * 100)

primeiro = int(input("PRIMEIRO TERMO:"))
razao = int(input("RAZAO da PA:"))
termo = primeiro
cont = 1

while  cont <= 10:
    print("{}".format(termo) ,end=" > ")
    termo += razao
    cont += 1
print(" ACABOU .")