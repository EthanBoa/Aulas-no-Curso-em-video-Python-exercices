#Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

idademedia = 0
maioridadehomem = 0
nomevelho = ""
mulheresmenosde20 = 0
for p in range(1, 5):
    print("---------- {} pessoa ---------".format(p))
    nome = str(input("Nome:")).strip()
    idade = int(input("Idade:"))
    sexo = str(input("Sexo [M/F]:")).strip()
    idademedia += idade / 4

    if p == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome

    if sexo in "Mm" and idade > maioridadehomem:
            maioridadehomem =idade
            nomevelho = nome

    if sexo in "Ff" and idade < 20:
        mulheresmenosde20 += 1

print("A idade media do grupo e {} anos. \n O homem mais velho e {} e tem {} anos. \nAo todo tem {} mulheres abaixo de 20 anos.".format(idademedia, nomevelho, maioridadehomem, mulheresmenosde20))
