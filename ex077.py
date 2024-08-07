#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')


for l in palavras:
    print(f"\nNa palvra {l.upper}  ", end ="")

    for letter in l:
        if letter.lower() in 'aeiou':
            print(f"{letter}", end ="")