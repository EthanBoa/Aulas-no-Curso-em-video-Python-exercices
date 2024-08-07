#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = list()

while True:
    n = int(input("Digite um numero:"))
    if n not in lista:
        lista.append(n)
        print("Valor adicionado com sucesso")
    else:
        print("valor ja digitado! Nao sera adicionado novamente a lista.")

    resposta = " "
    while resposta not in "S""N":
        resposta = str(input("Quer continuar? [S/N]:")).strip().upper()[0]
        
    if resposta == "N":
        break

print("-="*30)
print(f"Voce digitou os valores {sorted(lista)}")
