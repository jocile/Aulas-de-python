print("Olá, seja bem-vindo ao Test Bank. Antes de você ingressar na sua conta, iremos pedir seu CPF e sua senha.")
cpf = input("1-Digite seu cpf:->  ")
senha = input("2-Sua senha:->   ")

saldo = 1000.00  # Seu saldo disponível
transacoes = []  # Lista para armazenar transações

while True: 
    print("-------------Menu---------------\n")
    print("1-Digite. 'D' para depósito.\n")
    print("2-Digite. 'S' para saque.\n")
    print("3-Digite. 'E' para extrato.\n")
    print("4- Digite. 'EXIT' para sair. \n")

    acao = input("Qual sua escolha ? D,S,E ou EXIT->  ").upper()

    if acao == 'D':
        valor_deposito = input("Digite o valor do depósito: R$")
        try:
            valor_deposito = float(valor_deposito)
            if valor_deposito > 0:
                saldo += valor_deposito
                transacoes.append(f"Depósito: R${valor_deposito:.2f}")
                print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso.")
            else:
                print("Por favor, insira um valor positivo para o depósito.")
        except ValueError:
            print("Por favor, insira um valor numérico válido.")

    elif acao == 'S':
        valor_saque = input("Digite o valor do saque: R$")
        try:
            valor_saque = float(valor_saque)
            if valor_saque > saldo:
                print("Saldo insuficiente para realizar o saque.")
            else:
                saldo -= valor_saque
                transacoes.append(f"Saque: R${valor_saque:.2f}")
                print(f"Saque de R${valor_saque:.2f} realizado com sucesso.")
        except ValueError:
            print("Por favor, insira um valor numérico válido.")

    elif acao == 'E':
        print("\n--- Extrato ---")
        for transacao in transacoes:
            print(transacao)
        print(f"Saldo atual: R${saldo:.2f}\n")

    elif acao == 'EXIT':
        print("Até breve caro cliente!")
        break

    else:
        print("Ação inválida. Tente novamente.")