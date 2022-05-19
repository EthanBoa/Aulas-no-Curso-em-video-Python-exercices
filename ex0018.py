import math
from math import sin, cos, tan
a = float(input("Qual e o valor do angulo:"))
s = sin(math.radians(a))
c = cos(math.radians(a))
t = tan(math.radians(a))
print("O valor do seno e {:.2f} \n O valor do cosseno e {:.2f}\n  O valor da tangente e {:.2f}".format(s, c, t))
