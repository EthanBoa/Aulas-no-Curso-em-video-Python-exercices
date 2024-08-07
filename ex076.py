#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.



lista = ("Lapis", 10, 
        "Caneta", 15,
        "Livro", 750,
        "Borracha", 5,
        "Afiador", 10,
        "Estojo", 110,
        "Reguas", 55,
        "Pasta", 1400,
        "Compasso", 75)

print("-" * 30)
print("LISTAGEM DE PRECOS")
print("-" * 30)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f"{lista[pos]:.<30}", end="")
    
    else:
        print(f"R${lista[pos]:>3}")