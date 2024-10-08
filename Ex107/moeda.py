#


def aumentar (a):
    """
        -> A funcao dobro retorna o dobro de qualquer numero real.
            Param a: O valor a ser adicionado 10%.
            Param aumento: O valor do aumento.
    """


def dobro(num):
    """
        -> A funcao dobro retorna o dobro de qualquer numero real.
            Param num: O valor a ser  duplucado
    """
    num *= 2
    return num

def diminuir(d):
    """
        -> A funcao diminuir retorna a diminuicao de 10% de qualquer numero real.
            Param d: O valor a ser diminuido.
            Param divisor: O valor da diminuicao.
    """
    divisor = ((d*10)/100)+d
    return divisor

def metade (m):
    """
        -> A funcao dobro retorna o dobro de qualquer numero real.
            Param m: O valor a ser dividido a metade.
    """
    m /= 2
    return m




print(dobro(10))
print(metade(10))
print(diminuir(10))