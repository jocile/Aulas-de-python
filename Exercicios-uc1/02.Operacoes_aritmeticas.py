'''
Faça um algoritmo para ler três números e
 imprimir a soma, média e produto dos números lidos.
'''

# Entre com o primeiro número
n1 = float(input('Entre com o primeiro número: '))

# Entre com o segundo número
n2 = float(input('Entre com o segundo número: '))

# Entre com o terceiro número
n3 = float(input('Entre com o segundo número: '))

# Mostre a soma dos números
soma = n1 + n2 + n3
print(f'A soma dos números é: {soma}')

# Mostre a média dos números
media = soma / 3
print(f'A média dos números é: {media}')

# Mostre produto dos números
produto = n1 * n2 * n3
print(f'O produto dos números é: {produto}')
