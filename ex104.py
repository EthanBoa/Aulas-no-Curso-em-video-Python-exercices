#Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(msg):
    while True:
        ok= False
        valor = 0
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[1;31m ERRO! Digite um numero VALIDO!\033[m")
        
        if ok:
            break
    return valor


n = leiaInt("Digite um numero: ")
print(f"Voce digitou o numero {n}.")