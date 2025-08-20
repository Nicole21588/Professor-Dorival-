import math

def volume_cilindro(raio, altura ):

    return math.pi * (raio ** 2) * altura

raio = float(input("digite o raio do cilindro:"))

altura = float(input("digita a altura do cilindro:"))

print("o volume do cilindro é:", volume_cilindro(raio,altura))