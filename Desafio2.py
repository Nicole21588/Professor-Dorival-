def simular_banco():
    contas = {}  

    while True:
        print("\n=== MENU BANCO ===")
        print("1 - Criar conta")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Mostrar saldo")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome da conta: ")
            if nome in contas:
                print("Essa conta já existe.")
            else:
                saldo = float(input("Digite o saldo inicial: "))
                contas[nome] = saldo
                print("Conta criada com sucesso!")

        elif opcao == "2":
            nome = input("Nome da conta: ")
            if nome in contas:
                valor = float(input("Valor para depósito: "))
                contas[nome] += valor
                print("Depósito realizado. Saldo atual:", contas[nome])
            else:
                print("Conta não encontrada.")

        elif opcao == "3":
            nome = input("Nome da conta: ")
            if nome in contas:
                valor = float(input("Valor para saque: "))
                if valor <= contas[nome]:
                    contas[nome] -= valor
                    print("Saque realizado. Saldo atual:", contas[nome])
                else:
                    print("Saldo insuficiente.")
            else:
                print("Conta não encontrada.")

        elif opcao == "4":
            nome = input("Nome da conta: ")
            if nome in contas:
                print("Saldo da conta", nome, ":", contas[nome])
            else:
                print("Conta não encontrada.")

        elif opcao == "5":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida, tente de novo.")



simular_banco()




