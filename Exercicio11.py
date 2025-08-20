import math

def hipotenusa(cateto1, cateto2):
    return math.sqrt(cateto1**2 + cateto2**2)

cateto1 = float(input("digite o valor do primeiro cateto:"))

cateto2 = float(input("digite o valor do segundo cateto:"))


print("a hipotenusa do triangulo é:", hipotenusa(cateto1, cateto2))
