from math import hypot
ca =float(input("Qual e o valor do cateto adjacente:"))
co = float(input("Qual e o valor do cateto oposto:"))
h = hypot(ca, co)
print("O valor da hipotenusa e: {}".format(h))
