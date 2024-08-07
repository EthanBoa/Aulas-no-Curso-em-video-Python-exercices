#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
'''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep

primeiro = int(input("Digite o primeiro valor:"))
segundo = int(input("Digite o segundo valor:"))
opcao = 0

while opcao != 5:
    print(""""
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa""""")
    opcao = int(input(">>>>> Qual e a opcao?"))

    if opcao == 1:
        print(" A soma de {} + {} e {}.".format(primeiro, segundo, primeiro + segundo))
        sleep(1)

    elif opcao == 2:
         print(" O produto de {} * {} e {}.".format(primeiro, segundo, primeiro * segundo))
         sleep(1)

    elif opcao == 3:
        if primeiro > segundo:
            print(" O maior numero entre  {} e  {} e {}.".format(primeiro, segundo, primeiro))
        elif segundo > primeiro:
            print(" O maior numero entre  {} e  {} e {}.".format(primeiro, segundo, segundo))
        else:
            print("Os numeres sao iguais.")
        sleep(1)

    elif opcao == 4:
        print("Informe os numero novamente:")
        sleep(1.2)
        primeiro = int(input("Digite o primeiro valor:"))
        segundo = int(input("Digite o segundo valor:"))
        sleep(1)
        
    elif opcao == 5:
        print("Finalizando...")
        sleep(3)
        print("Fim do programa! Come back!")

    else:
        print("Opcao invalida! Tente novamete")

    print("=-"*15)
