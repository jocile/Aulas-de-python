lista_compras = []
valor_total = 0

while True:
    produto = input("Digite o nome do produto (ou 'fim' para encerrar):")
    if produto.lower() == 'fim':
        break
    valor = float(input("Digite o valor do produto: "))
    lista_compras.append((produto, valor))
    valor_total += valor
    
print ("\n Lista de compras:")
for item, valor in lista_compras:
    print(f"{item}: R${valor:.2f}")
    
print (f"\n Valor total da compra: R${valor_total:.2f}")