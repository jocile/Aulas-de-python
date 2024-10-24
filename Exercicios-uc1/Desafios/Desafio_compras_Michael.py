'''
Crie uma lista com os itens e o valor para uma compra de um supermercado;
Mostre a lista e o valor total da compra.
'''

compras = {}

while True:
    # Nome do produto
    produto = input("Digite o nome do produto (ou 's' para finalizar): ")
    if produto.lower() == 's':
        break
    # Valor do produto
    valor = float(input("Digite o valor do produto: R$ "))

    # Adiciona o produto e seu valor
    compras[produto] = valor

# somatório de tudo 
total = sum(compras.values())

# Lista de compras e o valor total
print("\n### Lista de Compras ###")
for item, valor in compras.items():
    print(f"{item}: R$ {valor:.2f}")

print(f"\nValor Total: R$ {total:.2f}")