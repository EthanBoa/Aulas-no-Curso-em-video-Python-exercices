# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.
n = str(input("Qual e o seu nome?")).strip()
print("O seu nome com todas letras maisculas fica:", n.upper())
print("O seu nome com todas letras menusculas fica:", n.lower())
print("O seu nome tem em todo {} letras".format(len(n) - n.count(" ")))
print("O seu primeiro nome tem {} letras".format(n.find(" ")))
