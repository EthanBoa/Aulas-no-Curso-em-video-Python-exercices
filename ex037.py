#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
n = int(input("Digite um numero inteiro:"))
print('''Escolha uma das Bases para a conversao:
[ 1 ] Converter para BINARIO:
[ 2 ] Converter para OCTAL:
[ 3 ] Converter para HEXADECIMAL:
 ''')
o = int(input("Opcao numero?"))

if o == 1:
    print("{} Convertido em BINARIO fica {}.".format(n, bin(n) [2:]))

elif o == 2:
    print("{} Convertido em OCTAL fica {}.".format(n, oct(n) [2:]))

elif o == 3:
    print("{} Convertido em HEXADECIMAL fica {}.".format(n, hex(n) [2:]))
    
else:
    print("Opcao invalida tente novamente.")