#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. 
# No final, mostre:                                                                                                    
#  A) Quantas pessoas foram cadastradas.                                                                                                              
#  B) Uma listagem com as pessoas mais pesadas.                                                                                                  
#  C) Uma listagem com as pessoas mais leves.


galera = []
lista = []
maior = menor =0
while True:
    galera.append(str(input("Nome:")))
    galera.append(float(input("Peso:")))

    if len(lista) == 0:
        maior =  menor = galera
        
    else:
        if galera[1] > maior:
            maior = galera[1]

        if galera[1] < menor:
            menor = galera[1]

    lista.append(galera[:])
    galera.clear()
    
    resp = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]

    if resp == "N":
        break

print("=-" *30)
print(f"Vc cadastrou {len(lista)} pessoas.")
print(f"O maior peso foi de {maior}Kg. Peso de ", end = " " )
for p in lista:
    if p[1] == maior:
        print(f"[{p[0]}]", end=" ")

print()

print(f"O menor peso de {menor}Kg. Peso de ", end = " ")
for p in lista:
    if p[1] == menor:
        print(f"[{p[0]}]", end=" ")


