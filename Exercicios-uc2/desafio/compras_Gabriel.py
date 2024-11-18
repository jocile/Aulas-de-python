'''
Repositório do projeto:
https://github.com/Gabriel0726/CRUD---Compras/tree/main/CRUD-Compras
'''

# Inicializando a lista de compras
compras = []


# Função para exibir o menu
def exibir_menu():
    print("\nEscolha uma opção:")
    print("1 - Continuar inserindo itens")
    print("2 - Parar e finalizar a compra")


# Loop para inserir os itens na lista
while True:
    # Solicitando o nome do item
    item = input("\nDigite o nome do item: ")

    # Solicitando o valor do item
    try:
        valor = float(input(f"Digite o valor de {item}: R$ "))
    except ValueError:
        print("Por favor, insira um valor numérico válido para o item.")
        continue

    # Adicionando o item e seu valor à lista
    compras.append((item, valor))

    # Exibindo o menu
    exibir_menu()

    # Solicitando a escolha do usuário
    escolha = input("Digite a opção (1 para continuar, 2 para parar): ")

    if escolha == '2':
        break
    elif escolha != '1':
        print("Opção inválida. Digite 1 para continuar ou 2 para parar.")

# Exibindo os itens inseridos e o total
print("\nLista de compras:")
total = 0
for item, valor in compras:
    print(f"{item}: R$ {valor:.2f}")
    total += valor

print(f"\nTotal da compra: R$ {total:.2f}")
