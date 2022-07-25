 #Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
n = str(input("Qual e o seu nome?")).strip()
m = n.split()
print('Muito prazer e te conhecer!')
print("O seu primero nome e {}".format(m[0]))
print("O seu ultimo nome e {}".format(m[len(m)-1]))
