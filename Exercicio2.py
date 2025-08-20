def calcular_imc(peso, altura):

    imc = peso / (altura ** 2)

    return imc 

peso = float(input("digite seu peso:"))

altura = float(input("digite sua altura:"))


print(" o imc é:", calcular_imc( 70, 1.75))