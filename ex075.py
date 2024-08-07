#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

count = 0

num = (int(input("Digite um numero:")), 
        int(input("Digite um numero:")), 
        int(input("Digite um numero:")), 
        int(input("Digite um numero:")))
print(f"Voce digitou os seguintes valores: {num} \nO 9 apareceu {num.count(9)} vezes.")
if num == 3:
    print(f"O 3 apareceu na {num.index(3)+1} posicao.")

else:
    print("O 3 nao foi digitado.")

print("Os numeros pares ditados foram: ", end=" ")

for n in num:
    if n % 2 == 0:
        print(n, end=" ")
