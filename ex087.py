'''
Exercício Python 087: Aprimore o desafio anterior, mostrando no final:                                                  
   A) A soma de todos os valores pares digitados.                                                                                                  
   B) A soma dos valores da terceira coluna.                                                                                                                
   C) O maior valor da segunda linha.
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar=maior=scol= 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um valor pra [{l},{c}]:"))

print("-="*30)
 
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]", end=" ")
        if matriz[l][c] % 2== 0:
            spar += matriz[l][c]
    print()
print("-="*30)

for l in range(0,3):
    scol += matriz[l][2]

for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]

    elif matriz[1][c] > maior:
        maior = matriz[1][c]


print(f"A soma dos nr pares e {spar}.")
print(f"A soma dos valores da 3 coluna e {scol}.")
print(f"O maior valor da linha 2 e {maior}")
    

