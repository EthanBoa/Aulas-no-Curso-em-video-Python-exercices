# Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
n = str(input("Digite uma frase:")).strip()
print("A letra 'A' a parace {} vezes.".format(n.lower().count('a')))
print("A primeira letra 'A' apareceu na posicao {} .".format(n.find('a')))
print("A ultima letra 'A' apareceu na ultima vez na posicao {}".format(n.rfind('a')))
