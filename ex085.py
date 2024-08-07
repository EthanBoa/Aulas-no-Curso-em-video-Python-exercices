#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista = [[], []]
nr = 0
for n in range(1, 8):
    nr = int(input(f"Digite o {n}o numero:"))

    if nr % 2 ==0:
        lista[0].append(nr)

    else:
        lista[1].append(nr)

print("-="*30)

lista[0].sort()
lista[1].sort()

print(f"Os valores pares digitados foram: {lista[0]}")
print(f"Os valores impares digitados foram: {lista[1]}")

   
