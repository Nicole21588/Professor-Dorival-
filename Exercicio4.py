import math

def distancia_pontos(x1, y1, x2, y2):

    return math.sqrt((x2 - x1)** 2 + (y2 - y1) ** 2 )

x1 = float(input("digite x1"))

y1 = float(input("digite y1"))

x2 = float(input("digite x2"))

y2 = float(input("digite y2"))


print("a distancia entre os pontos e:", distancia_pontos(x1, y1, x2, y2))