#Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n, show= False):
    from time import sleep
    f = 1
    for c in range(n,0,-1):
        if show:
            print(f"{c}",end="", flush= True)
            sleep(0.3)
            if c > 1:
                print(" x ",end="", flush= True)
                sleep(0.3)
            else:
                print(" =",end=" ", flush= True)
                sleep(0.3)

        f*=c
    return f
print(fatorial(4,show=True))