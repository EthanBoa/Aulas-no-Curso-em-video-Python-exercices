#Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.


'''for p in range(1, 50+1):
    if p % 2 == 0:
        print(p, end="  ")

print("FIM!!!!!!!!!")'''

for p in range(2, 50, 2):
    print(p, end=" ")
print("FIM!!")