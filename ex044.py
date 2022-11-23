#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros

#NOTA: p= preco ;  d= disconto ;  t= total;  o= opcao;  j= juros



print(" LOJAS ETHAN ")

p = float(input("PRECO DAS COMPRAS:"))
print('''FORMAS DE PAGAMENTO:
[ 1 ] a vista/ cheque:
[ 2 ] a vista no catao:
[ 3 ] 2x no carrtao:
[ 4 ] 3x ou mais no cartao:
 ''')
o = int(input("Opcao numero?"))

if o == 1:
    d = p - (0.10 * p)

elif o == 2:
    d = p - (0.05 * p)

elif o == 3:
    t = p
    parcela = t / 2
    print("A sua compra ser parcelada em 2x de {:.2f}mts.".format(parcela))
    
elif o == 4:
    l= int(input("Quantas parcelas?"))
    j = p + (p * 0.2)
    total = p/l
    print("A sua compra parcerlada em {}x sera de {:.2f}mts".format(l, j))

else:
    t = 0
    print("Opcao invalida tente novamente.")

print("A compra que custava {:.2f}mts passara a custar {:.2f}mts.".format(p, d or j ))

