#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
pares = []
impares = []
while True:
    lista.append(int(input("Digite um numero:")))
    resp = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    
    if resp == "N":
        break

for i , v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
        
    elif v % 2 == 1:
        impares.append(v)  

print("-="*30)
print(f"A lista completa e {lista}.")
print(f"A list dos numeros pares e {pares}")
print(f"A list dos numeros impares e {impares}")