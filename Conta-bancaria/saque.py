'''
Receba o valor do saque e compare com o saldo da conta bancária
'''
saldo_inicial = 1000
saldo = saldo_inicial
saque = float(input('Digite o valor do saque: '))
if saque <= saldo_inicial:
    print('Saque realizado com sucesso!')
    saldo = saldo_inicial - saque
else:
    print('Saldo insuficiente!')

print(f'Saldo atual: {saldo}')