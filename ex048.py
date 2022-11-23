#Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0 #Acumulador 
cont = 0 #Contador
for m in range(1,501,2):
    if m %3 == 0:
        cont = cont + 1
        soma = soma + m
 
print("A soma dos {} valores solicitados e {}.".format(cont, soma))
