#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.                  Depois disso, mostre:                                                                                                                                                A) Quantos números foram digitados.                                                                                                                    B) A lista de valores, ordenada de forma decrescente.                                                                                          C) Se o valor 5 foi digitado e está ou não na lista.

count = 0
lista = []

while True:
    num = int(input("Digite um numero:"))
    count += 1
    if num not in lista:
        lista.append(num)
    resp= " "
    while resp not in "S""N":
        resp = str(input("Quer continuar? [S/N]:")).strip().upper()[0]
        
    if resp == "N":
        break
    
print("-="*30)
print(f"Vc digitou {count} numeros.")

lista.sort(reverse=True)
print(f"A lista em ordem decrescente fica {lista}")

print("O valor 5 esta na lista" if 5 in lista else (print("O valor 5 nao esta na lista.")))