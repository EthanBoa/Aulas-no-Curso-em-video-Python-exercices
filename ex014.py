#Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
c = float(input('Qual e a temperatura em °C?'))
t = c * 1.8 + 32
print('A sua tempratura em °F e de {}°F'.format(t))
