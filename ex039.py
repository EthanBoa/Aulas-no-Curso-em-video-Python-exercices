#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

a = date.today().year

n = int(input('Ano de nascimento:'))

i = ( a - n )

print("Quem nasceu em {} tem {} anos em {}".format(n, i, a ))

if n == 18:

    print("Vc deve se alistar  \033[31;41mIMEDIATAMENTE\033[m")

elif i < 18:

    s = 18 - i

    print("Ainda faltam {} anos.".format(s))

elif i > 18:

    s = i - 18 

    print("vc deveria ter se alistado a {} anos.".format(s))

