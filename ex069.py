#Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

print('-'*30)
print("     CADASTRO DE PESSOAS       ")
print('-'*30)

idade = pessoas = homem = mulher = 0

while True:
    print('-'*30)
    idade = int(input("IDADE:"))

    sexo = " "
    while sexo not in "MF":
        sexo = str(input("SEXO [M/F]:")).strip().upper()[0]
        print('-'*30)
    if idade >= 18:
            pessoas += 1
            
    if sexo == "M":
            homem += 1

    if sexo == "F" and idade < 20:
            mulher += 1

    resp = " "
    while  resp not in "SN":
        print('-'*30)
        resp = str(input("Quer continuar? [S/N]:")).strip().upper()[0]
        print('-'*30)
    
    if resp == "N":
        break

print(f"Tem no total {pessoas} maiores de 18 anos.\nNo total foram cadastrados {homem}. \nTem no total {mulher} com menos de 20 anos.")



