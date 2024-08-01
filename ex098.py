'''Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:                                                                                                                                                                            a) de 1 até 10, de 1 em 1                                                                                                                                              b) de 10 até 0, de 2 em 2                                                                                                                                            c) uma contagem personalizada

Aula Anterior
'''


from time import sleep

def separador():
    print("="*40)


def contagem (i, f, p):
    print(f"Contagem de {i} ate {f} de {p} em {p}")

    count = i
    while count <=f:
        print(f"{count}", end =" ")
    
        count += p
        sleep(0.5)
    print("Fim")

separador()
contagem(1, 10, 1)
sleep(1)
separador()
contagem(1, 10, 2)
separador()
sleep(3)
print("Agora e a sua vez personalize a sua cantagem")
i = int(input("Inicio: "))
f = int(input("Final: "))
p = int(input("Passo: "))

