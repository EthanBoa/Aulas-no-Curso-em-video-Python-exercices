#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.



numeros = list()

for n in range(0, 5):
    numeros.append(int(input("Digite um numero:")))

print("-="*30)
print(f"A lista declarada foi {numeros}")
print(f"O maior numero lido foi {max(numeros)} \nO menor numero lido foi {min(numeros)}.")