''' 
Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.
'''

saldo_inicial = 0
saldo = saldo_inicial
extrato = []

def mostrar_menu():  
  return ''' 
  O QUE DESEJA?
  [d] Depositar
  [s] Sacar
  [e] Extrato
  [x] Sair

  Digite a inicial da função desejada: 
  '''

def depositar(saldo):
  deposito = float(input('Digite o valor desejado para o despósito: R$ '))
  saldo += deposito
  extrato.append(f'Depósito: R$ {deposito}')
  if deposito > 0:
    print('Depósito realizado com sucesso!')
  else: 
    print('Não foi possível realizar o depósito!')

def sacar(saldo):
  saque = float(input('Digite o valor que deseja sacar: R$ ')) 
  if saque <= saldo: 
    print('Saque realizado com sucesso!')
    extrato.append(f'Sacou: R$ {saque}')
    saldo = saldo - saque
  else: 
    print('Saldo insuficiente!')

def mostrar_extrato():
  # FIXME Faltou mostrar o saque e o saldo final
  print(f'extrato da sua conta: {extrato}')




while True:
    selecionado = input(mostrar_menu())
    if selecionado == 'd': #deposito
        depositar(saldo) 
    if selecionado == 's': #saque
        sacar(saldo)
    if selecionado == 'e': #extrato
        mostrar_extrato()
    if selecionado == 'x': break    
        