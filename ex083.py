#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

contador = 0
expressão = str(input('Digite a expressão:'))

for p in expressão:

    if p in '()':
        contador += 1

if contador % 2 == 0:
    print('Expressão Válida!')
    
else:
    print('Expressão Inválida')