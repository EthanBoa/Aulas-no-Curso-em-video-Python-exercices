#Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
num = ( " Zero" , "Um" , "dois" , "tres" , "quatro" , "cinco" , "seis" , "sete" , "oito" , "nove" , "dez" , "onze" , "doze"
 , "treze" , "catorze" , "quinze", "desasseos" , "desassete " , "dezoito" , "dezanove" , "vinte" )
while True:
    num1 = int(input('Digite um numero de 0 - 20:'))


    if  0 <= num1 <=20:
        break
    else:
        n1 = int(input("Por favor! Digite um numero de 0 - 20: "))
print(f"vc escrveu {num[num1] } na tela")

