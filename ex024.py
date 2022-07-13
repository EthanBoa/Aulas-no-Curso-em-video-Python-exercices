# Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
c = str(input("Qual e a sua cidade:")).strip()
print(c[:5].lower() == "santo")
