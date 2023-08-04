menu = """
        ===========MENU==========
        1- Depositar
        2- Sacar
        3- Extrato
        0- Sair
        =========================
        """

saldo = 0
LIMITE_SAQUE = 500
extrato = {}
numero_saques = 0
total_extrato = 0
LIMITE_NUMERO_SAQUES = 3


while True:
    selecionar = int(input(menu))

    if selecionar == 1:
        deposito = float(input("\nDigite a quantidade a depositar: "))
        if deposito < 0:
            print("\nValor inválido")
        else:
            saldo += deposito
            print(f"\nDepósito efetuado com sucesso! Novo saldo:R${saldo:.2f}")
            extrato[total_extrato] = f"Depósito +R${deposito:.2f}"
            total_extrato += 1
    
    elif selecionar == 2:
        saque = float(input(f"\nSaldo disponível:R${saldo:.2f}\nDigite o valor a ser sacado: "))

        if saque > saldo:
            print("\nSaldo insuficiente.")
        elif saque > LIMITE_SAQUE:
            print("\nSaque excedeu o limite.")
        elif numero_saques >= LIMITE_NUMERO_SAQUES:
            print("\nNumero de saques atingido.")
        else:
            saldo -= saque
            print(f"\nSaque efetuado, novo saldo:R${saldo:.2f}")
            extrato[total_extrato] = f"Saque    -R${saque:.2f}"
            total_extrato += 1
            numero_saques += 1
    
    elif selecionar == 3:
        print("Extrato:")
        for i in range(total_extrato):
            print(extrato[i])
        print(f"Saldo:   R${saldo:.2f}")
    
    elif selecionar == 0:
        break
    
    else:
        print("\nOpção não existente")
        