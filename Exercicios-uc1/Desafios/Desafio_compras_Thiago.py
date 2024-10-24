#Desafio - Total de Compras
'''O desafio consiste em somar os itens de uma lista de compras'''

#1ª Fase - Criar uma Lista
produtos = {'Shampoo': 19.90, 'Creme': 12.80,'Gel': 9.30,'Perfume': 49.90,'Sabonete':35.10,'Desodorante':14.90,'Hidratante':12.90,'Colônia': 59.90}

#2ª Fase - Criando o Pedido
#2.1 - exibindo a lista de produtos:
print('Produtos Disponíveis:')
for produto, valor in produtos.items():
    print(f"{produto}: R$ {valor:.2f}")

#2.2 - Carrinho de Compras
carrinho = []
total = 0.0

#2.3 - Loop de input pra seleção de produtos:
while True:
    escolha = input("Digite o nome do produto, use 'fechar' para finalizar a compra:")
    if escolha == 'fechar':
        break
    elif escolha in produtos:
        carrinho.append(escolha) #adiciona o produto ao carrinho
        total += produtos[escolha] #soma o valor do produto ao total
        print(f'{escolha} adicionado ao carrinho. Total parcial: R$ {total:.2f}')
    else:
        print("Produto não encontrado. Tente novamente.")

#3ª Fase - Exibindo o Total das Compras
print("\nProdutos escolhidos:", ', '.join(carrinho))
print(f"Total da compra: R$ {total:.2f}")