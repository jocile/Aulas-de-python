''' 
Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.
'''

menu = ''' 

O QUE DESEJA?
[d] Depositar
[s] Sacar
[e] Extrato
[x] Sair

Digite a inicial da função desejada: 
'''

saldo_inicial = 0
saldo = saldo_inicial
extrato = []

while True:
    selecionado = input(menu)
    if selecionado == 'd': #deposito
        deposito = float(input('Digite o valor desejado para o despósito: R$ '))
        saldo += deposito
        extrato.append(f'Depósito: R$ {deposito}')
        if deposito > 0:
            print('Depósito realizado com sucesso!')
        else: 
            print('Não foi possível realizar o depósito!') 
    if selecionado == 's': #saque
        saque = float(input('Digite o valor que deseja sacar: R$ '))
        extrato.append(f'Sacou: R$ {saque}')
        if saque <= saldo: 
            print('Saque realizado com sucesso!')
            saldo = deposito - saque
        else: 
            print('Saldo insuficiente!')
    if selecionado == 'e': #extrato
        print(f'extrato da sua conta: {extrato}')
    if selecionado == 'x': break    
        