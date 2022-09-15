#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
n = int(input(" Me diga um numero qualquer:"))
r = n % 2
if r == 0 :
    print("O numero {} e Par".format(n))
else:
    print("O numero {} e Impar!".format(n))
    

