#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

a = float(input("Primeiro lado:"))
b = float(input("Segundo lado:"))
c = float(input("Terceiro lado:"))
from time import sleep
print("\033[43m+=\033[m"*30)

print("\033[35mAnalizando os dados...\033[m")
sleep(3)
 
print("\033[43m+=\033[m"*30)

#Possibilidades de formar triangulos.
if ( a + b >= c and b + c >= a and a + c >= b ):
    print("\033[36;40mEsse dados podem formar um triangulo\033[m", end= " ")

    if a != b != c !=a :
        print("\033[31;40m ESCALENO.\033[m")
    
    elif a == b == c:
        print("\033[32;40m EQUILATERO\033[m")

    else:
        print("\033[36;40m ISOSCELES\033[m")


#Caso os dados nao formem trinagulo.
else:
    print("\033[41mEsse dados nao podem formar um triangulo.\033[m")
