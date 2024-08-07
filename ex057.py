#Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.


s = str(input(" Digite o seu sexo [ M/F ]:")).strip().upper()[0]
while s not in 'M F':
    s = str(input("Dados invalido. Por favor digite o seu sexo:")).strip().upper()[0]

print("Sexo {} digitado com sucesso.".format(s))
