#Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print ("=" * 100)
print ("                                    TERMOS DE UMA PA:                                     ")
print("=" * 100)

primeiro = int(input("PRIMEIRO TERMO:"))
razao = int(input("RAZAO da PA:"))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while  cont <= total:
        print("{}".format(termo) ,end=" > ")
        termo += razao
        cont += 1
    print(" Pausa ")
    mais = int(input("Quanto mais termos vc quer adicionar:"))
print("Progrecao finalizada com {} termos mostrados.".format(total))

    
