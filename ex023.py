n = int(input('Diguite um numero :'))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(" Anaisando o numero {} ".format(n))
print(f"Unidade: {u} ")
print(f"Dezena: {d} ")
print(f"Centena: {c} ")
print(f" Milhares: {m} ")
