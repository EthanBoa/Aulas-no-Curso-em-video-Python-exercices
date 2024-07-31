# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
dic = {}

dic["nome"] = str(input("Nome:"))

dic["ano"] = int(input("Ano de Nascimento:"))

dic["cart_trab"] = int(input("Carteira de Trabalho (0 nao tem):"))


if dic["cart_trab"] == 0:
    print("-="*30)
    print(f"       -O nome tem valor {dic['nome']}.")
    print(f"       -A idade tem valor {datetime.now().year-dic['ano']}.")
    print(f"       -O ctps tem valor {dic['cart_trab']}.")
    
if dic["cart_trab"] > 0:
    
    dic["ano_contra"] = int(input("Ano de contratacao: "))

    dic["salario"] =  float(input("Salario: R$"))
    
    print("-="*30)
    print(f"       -O nome tem valor {dic['nome']}.")
    print(f"       -A idade tem valor {datetime.now().year-dic['ano']}.")
    print(f"       -O ctps tem valor {dic['cart_trab']}.")
    print(f"       -O ano de contratacao tem valor {dic['ano_contra']}.")
    print(f"       -O salario tem valor {dic['salario']}.")
    print(f"       -Vai se aposentar com {(datetime.now().year-dic['ano'])+(dic['ano_contra']+35)-datetime.now().year}.")
print("-="*30)