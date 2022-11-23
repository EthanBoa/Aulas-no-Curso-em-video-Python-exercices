#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO

n = float(input('Digite a nota da  1 ACS:'))
n1 = float(input('Digite a nota da 2 ACS:'))
m = (n + n1 ) / 2
print('A sua media e {}'.format(m))

if m < 5:
    print("Aluno esta \033[0;31;41mREPROVADO\033[m")

elif  5 > m < 6.9:
    print("Aluno esta em \033[0;34;40mRECUPERACAO\033[m")

elif  m > 7:
    print("Aluno esta \033[0;32;40mAPROVADO\033[m")

