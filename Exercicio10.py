import math 

def area_circulo(raio):

    return math.pi * (raio ** 2)

raio = float(input("digite um valor do raio do circulo:"))

print("a area do circulo é:", area_circulo(raio))