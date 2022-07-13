#  Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
d = float(input('Quantos dias vc andou com o carro?'))
k = float(input('Quantos kilometors vc andou?'))
s = d * 60 + k * 0.15
print(' O valor a pagar e de {}R$'.format(s))
