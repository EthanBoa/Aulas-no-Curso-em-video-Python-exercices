# Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
v = float(input("Qual e a velocidade do seu carro atual:"))
if v > 80:
    print("Voce foi multado a multado! Atingiu o limite de velocidade de 80km/h")
    m = ( v - 80) * 7
    print("Vc tem que pagar uma multa de {:.2f}mts".format(m))
print("Tenha um boa dia! Dirija com seguranca!")
