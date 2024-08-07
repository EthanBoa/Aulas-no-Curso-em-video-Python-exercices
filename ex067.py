#Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    num = int(input("Quer ver a tabuada de  qual valor?"))

    if num < 0:
        print("\033[36mPROGRAMA DE TABUADA ENCERADO! VOLTE SEMPRRE :-)\033m")
        break

    print("=-"*50)
    for c in range(1, 11):

        print(f"{c} * {num} = {c * num}")

    print("=-"*50)
