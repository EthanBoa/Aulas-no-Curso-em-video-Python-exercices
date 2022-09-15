#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
c = float(input("Qual e o valor da casa:"))
s = float(input("Qual e o salario do comprador: "))
a = int(input("Em quantos anos o pagar quer pagar:")) 
p = c / (a * 12)
t = (s * 30 ) /100
print('Pra comprar uma casa de {:.2f} em {:.2f} anos a pretacao sera de {:.2f} mts '.format(c, a, p))
if p<=t:
    print("O emprestimo sera \033[36mCONCEDIDO\033{m")
else:
      print("O emprestimo foi \033[31mNEGADO\033[m")