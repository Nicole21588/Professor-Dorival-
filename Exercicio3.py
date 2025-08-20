import random

def gerar_numero_aleatorio(n, m):

    return random.randint(n, m)

n = int(input("digite o valor minimo:"))

m = int(input("digite o valor maximo:"))

print("numero aleatoriio gerado:", gerar_numero_aleatorio(n, m))