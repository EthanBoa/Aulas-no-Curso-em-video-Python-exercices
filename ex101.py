#Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.



def voto(ano):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - nascimento
    if idade < 17:
        return f"Com {idade} anos nao pode votar!"

    elif idade == 17 or idade >= 70:
        return f"O voto com {idade} anos e opicional."
    
    else:
        return f"Com {idade} anos o voto e OBRIGATORIO."
    
    
nascimento = int(input("Em que ano vc nasceu? "))
print(voto(nascimento))