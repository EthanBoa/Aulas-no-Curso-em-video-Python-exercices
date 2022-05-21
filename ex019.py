from random import choice
a = input("Qual o nome da primeiro aluno:")
b = input("Qual o nome da segundo aluno:")
c = input("Qual o nome da terceiro aluno:")
d = input("Qual o nome da querto aluno:")
l = [a, b, c, d]
e = choice(l)
print("O ecolhido e {}".format(e))
