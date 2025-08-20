def decimal_para_binario(numero):
    if numero == 0:
        print("0")
        return
    binario = ""
    while numero > 0:
        binario = str(numero % 2) + binario
        numero = numero // 2
    print(binario)

valor = int(input("digite um numero decimal"))

decimal_para_binario(17)  
