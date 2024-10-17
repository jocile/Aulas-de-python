'''
Faça um algoritmo para ler três números
e imprimir a soma, média e produto dos números lidos
'''

# Ler os três números
n1 = int(input('Entre com o primeiro número: '))
n2 = int(input('Entre com o segundo número: '))
n3 = int(input('Entre com o terceiro número: '))

# Calcular a soma
soma = n1 + n2 + n3

# Calcular a média
media = soma / 3

# Calcular o produto
produto = n1 * n2 * n3

# Mostrar os resultados
print(f'A soma dos números é: {soma}')
print(f'A média dos números é: {media}')
print(f'O produto dos números é: {produto}')
