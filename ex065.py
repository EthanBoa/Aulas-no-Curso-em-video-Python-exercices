#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

soma = count = media = 0
r = "S"
maior = 0
menor = 0

while r in "S": 
    n = int(input("Digite um numero:"))
    r = str(input("Quer continuar[S / N]?")).upper().strip()[0]
    count += 1
    soma += n
    if count == 1:
        maior =  menor = n
        
    else:
        if n > maior:
            maior = n

        if n < menor:
            menor = n

media = soma / count

print ("Voce digutou {} numeros. \nE o maior numero lido foi {} e o menor {}. \nA media dos numeros e {} . ".format(count, maior, menor, media ))
