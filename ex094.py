#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

pessoa = {}
Lista = []
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input("Nome: "))
    pessoa['idade'] = int(input("Idade: "))

    
    pessoa['sexo'] = str(input("Sexo [M/F]")).upper()[0]
    while pessoa['sexo'] not in "MF":
        print("ERRO! RESPONDA APENAS COM M OU F")
    soma += pessoa["idade"]
    continuar = str(input("Quer continuar?[S/N] ")).upper()[0]
    Lista.append(pessoa.copy())
    while continuar not in "SN":
        print("ERRO! Responda apenas com S ou N.")
    
    if continuar == "N":
        break

media = soma/len(Lista)
print("-="*50)
print(f"A) Ao todo temos {len(Lista)} cadastradas.")
print(f"A media da idade e {media:5.2f} anos.")

for p in Lista:
    if p["sexo"] == "F":
        print(f"C) As mulheres cadastradas foram: ", end = "")
        print(f"{p['nome']}, ")
for p in Lista:
    for k, v in p.items():
        if p["idade"] > media:
            print("D) As pessoas acima da media foram: ")
            print(f"       ===> Nome = {p['nome']} idade = {p['idade']};\n")
print("<< ENCERRADO >>")
