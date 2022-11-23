#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input("Digite um número para veres a sua taboada:"))
for c in range(1,13):
    print("{} x {} = {}".format(n, c, n * c))