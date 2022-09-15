#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = float(input("primeiro valor:"))
b = float(input("segundo valor:"))
c = float(input("Terceiro valor:"))
# Verificando o menor.
menor = a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c

maior=a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c

print("O menor numero intro duzido foi \033[7;35;41m{}\033[m".format(menor))
print("O maior numero introduzido foi o \033[7;36;43m{}\033[m".format(maior))

