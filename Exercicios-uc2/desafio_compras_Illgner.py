produtos = {'Arroz': 5.90, 
            'Macarrão': 3.60,
            'Feijão': 8.50,
            'Carne': 50.90,
            'Frango':20.00,}


print('Produtos Disponíveis:')
for produto, valor in produtos.items():
    print(f"{produto}: R$ {valor}")

#Carrinho
carrinho = []
total_compras = 0.0

while True:
    adicione = input("Digite o nome do produto, use 'x' para finalizar a compra: ")
    if adicione == 'x': break
    elif adicione in produtos:
        carrinho.append(adicione) #adiciona o produto ao carrinho
        total_compras += produtos[adicione] #soma o valor doso produtos adicionados
        print(f'{adicione} adicionado ao carrinho. Total até o momento: R$ {total_compras}')
    else:
        print("Produto não encontrado. Tente novamente.")

#Exibindo o Total das Compras depois que apertar 'x'
print("\nProdutos escolhidos:", ', '.join(carrinho))
print(f"Total da compra: R$ {total_compras}")


