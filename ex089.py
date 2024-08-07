#Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

lista = list()
count= 0


while True:
    nome = str(input("Nome:"))
    n1 = float(input("Nota1:"))
    n2 = float(input("Nota2:"))
    media = (n1 + n2) / 2
    count += 1
    stop = str(input("Quer continuar? [S / N]    ")).upper()
    lista.append([count,    nome,       [n1, n2],      media])

    if stop == "N":
        break
    
print("-="*40)
print("No.", end="       ""NOME", end="        ""MEDIA")
print("-"*40)

#print(lista)