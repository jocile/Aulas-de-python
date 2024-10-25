# Lista de compras com itens e seus valores
lista_compras = {
    "Arroz (1 kg)": 5.00,
    "Feijão (1 kg)": 7.00,
    "Macarrão (500 g)": 3.00,
    "Molho de tomate (340 g)": 4.00,
    "Óleo de soja (900 ml)": 6.00,
    "Açúcar (1 kg)": 4.00,
    "Sal (1 kg)": 2.00,
    "Leite (1 L)": 4.00,
    "Ovos (dozen)": 10.00,
    "Frango (1 kg)": 12.00,
    "Carne moída (1 kg)": 20.00,
    "Pão (500 g)": 5.00,
    "Queijo (500 g)": 15.00,
    "Frutas (maçã, 1 kg)": 6.00,
    "Legumes (cenoura, 1 kg)": 4.00,
}

# Cálculo do total
total = sum(lista_compras.values())

# Impressão da lista e do total
print("Lista de Compras:")
for item, valor in lista_compras.items():
    print(f"{item}: R$ {valor:.2f}")

print(f"\nTotal Aproximado: R$ {total:.2f}")