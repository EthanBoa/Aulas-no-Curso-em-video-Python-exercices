#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER

from datetime import date

actual = date.today().year

data = int(input("Diga o ano de nascimento:"))

i = (actual  - data )

print("O ")

if i <= 9 :
    print("CLASSIFICACAO: MERIM")

elif i > 9  and i <= 14:
    print("CLASSIFICACAO:INFANTIL")

elif i > 14 and i <= 19:
    print("CLASSIFICACAO:JUNIOR")

elif i > 19 and i <=25:
    print("CLASSIFICACAO:SENIOR")

elif i > 25:
    print("CLASSIFICACAO: MASTER.")
else:
    print(" Por favor coloque dados exactos! Volte a tentar.")