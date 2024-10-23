'''
Faça um algoritmo para ler dois números A e B e dizer se A é divisível por B
'''

# Entre com o primeiro número: 10
n1 = int(input('Entre com o primeiro número: '))

# Entre com o segundo número: 20
n2 = int(input('Entre com o segundo número: '))

# Mostre se o primeiro número é divisível pelo segundo número
resultado = 'é' if n1 % n2 == 0 else 'não é'

print(f" O número {n1} {resultado} divisível por {n2}")