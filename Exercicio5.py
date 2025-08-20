import math

def raio_circulo(area):

     return math.sqrt(area / math.pi)

area = float(input("digite a area do circulo"))

print("o raio do circulo é:", raio_circulo(area))