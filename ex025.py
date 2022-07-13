#  Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ele tem "SILVA" no nome.
n = str(input("Digite um nome:")).strip()
print(" Esse nome tem Silva? {}".format("silva " in n.lower()))
