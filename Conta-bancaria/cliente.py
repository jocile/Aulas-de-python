''' 
1 - O cliente do banco precisa entrar com os seguintes dados: 
  Nome, CPF, 
2 - Mostrar os dados do cliente
3 - Criar uma lista para salvar os dados do cliente
'''

nome = input('Digite o nome: ')
cpf = input('Digite o CPF: ')

cliente = [nome, cpf]
clientes = [cliente]

print(f'Cadastrado o nome: {nome} e CPF: {cpf}')

nome = input('Digite o nome: ')
cpf = input('Digite o CPF: ')

print(f'Cadastrado o nome: {nome} e CPF: {cpf}')

cliente = [nome, cpf]
clientes.append(cliente)

print('-----------------')

print("Clientes cadastrados: ")
print(f"Nome: {clientes[0][0]}")
print(f"CPF: {clientes[0][1]}")
print(f"Nome: {clientes[1][0]}")
print(f"CPF: {clientes[1][1]}")

print('-----------------')
