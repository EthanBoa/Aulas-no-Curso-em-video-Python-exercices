#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais

from time import sleep
from wsgiref.validate import InputWrapper
print ( "Digite um numero para que o computadar compare"
"NB: Um numero sem caracteres literais e nem outro qualquer")
p = float(input("Digite o primero valor:"))
i = float(input("Digite o segundo valor:"))

print("\033[34;45mAnalizando os valores por favour aguarde!\033[m")
sleep(3)

if p > i:
    print("O maior  numero e {}".format(p))

elif p < i:
    print("O maior numero e {}".format(i))

else:
   print("Não existe valor maior, os dois são iguais.") 

