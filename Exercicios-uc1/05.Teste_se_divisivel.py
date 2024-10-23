'''
Faça um algoritmo para ler dois números A e B e dizer se A é divisível por B
'''

# Entre com o primeiro número: 10
n1 = int(input('Entre com o primeiro número: '))

# Entre com o segundo número: 20
n2 = int(input('Entre com o segundo número: '))

# Mostre se o primeiro número é divisível pelo segundo número
if n1 % n2 == 0 :
  print(f" O número {n1} é divisível por {n2}")
else:
  print(f" O número {n1} não é divisível por {n2}")