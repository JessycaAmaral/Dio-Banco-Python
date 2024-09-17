menu = """\n
    -+-+-+-+-+-+ Banco Python +-+-+-+-+-+-
    **************** MENU ****************
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [0]\tSair
    => """
    
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("\tQual valor deseja depósito? "))

        if valor > 0:
            saldo += valor
            extrato += f"\tDepósito: R$ {valor:.2f}\n"

        else:
            print("\tErro! O valor inválido.")

    elif opcao == "2":
        valor = float(input("\tQual valor deseja sacar? "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\tErro! Saldo insuficiente.")

        elif excedeu_limite:
            print("\tErro! Valor do saque excede o limite.")

        elif excedeu_saques:
            print("\tErro! Número máximo de saques diario excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"\tSaque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("\tErro! Valor inválido.")

    elif opcao == "3":
        print("\n\t**************** EXTRATO ****************")
        print("\tSem movimentações." if not extrato else extrato)
        print(f"\n\tSaldo: R$ {saldo:.2f}")
        print("\t*****************************************")

    elif opcao == "0":
        break

    else:
        print("\tErro! Selecione uma operação válida.")