'''
Faça um algoritmo para ler três números e imprimir se estes podem ou não formar um triângulo.
Observação - Para formar os lados de um triângulo cada um dos valores tem que ser menor que a soma dos outros dois.
'''

# Leia os três lados do triângulo

print('Entre com os 3 números para os lados do triângulo')
l1 = int(input('lado 1 ->'))
l2 = int(input('lado 2 ->'))
l3 = int(input('lado 3 ->'))

print(f"Você digitou os números: {l1}, {l2}, {l3}")

# Testar se cada um dos lados é menor que a soma dos outros dois lados
triangulo = False
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
  triangulo = True
  
if triangulo:
  print("O teste dos lados mostra que representam um triângulo")
else:
  print("O teste dos lados mostra que os números digitados não representam um triângulo")
