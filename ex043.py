#Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida

p = float(input("insira o seu peso:   (Kg) "))
h = float(input("Insira a sua altura:  (m)"))
imc = p / (h ** 2)

print('O IMC da pessoa e de {:.1f} '.format(imc))

if imc <= 18.5 :
    print("O IMC esta abaixo peso.")

elif imc > 18.5 and imc <= 25:
    print("O IMC esta ideal.")

elif imc > 25 and imc <= 30:
    print("O IMC esta sobrepeso.")

elif imc > 30 and imc <=40:
    print("O IMC esta em Obesidade")

elif imc > 40:
    print(" IMC esta em Obesidade Morbida, Cuidado")
    
else:
    print(" Por favor coloque dados exactos! Volte a tentar.")