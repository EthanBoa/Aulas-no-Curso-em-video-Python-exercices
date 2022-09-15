#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
s = float(input("Quanto recebe o fucionario?"))
a = s + (15*s)/100
d = s + (10*s)/100
if s <= 1250:
    print("O salario do saldo fucionario com aumento de sera \033[34;46m{:.2f}\033[m".format(a))
else:
      print("O salario do saldo fucionario com aumento de sera \033[34;46m{:.2f}\033[m  ".format(d))