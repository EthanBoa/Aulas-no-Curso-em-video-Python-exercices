#Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

frase = str(input(" DIGITE UMA FRASE:")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = junto[::-1]

#OUTRA FORMA DE FAZER
'''inverso = "" 
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''
#FIM

print("O inverso de {} e {}.".format(junto, inverso))

if inverso == junto:
    print("TEMOS UM PALINDROME!")
else:
    print("A frase digitada nao e um palindrome.")
