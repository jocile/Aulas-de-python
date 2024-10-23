'''
Faça um algoritmo para ler um número inteiro e dizer se o número lido é par ou impar
'''
continuar = 's'
while continuar == 's':
  # Leia um número inteiro
  n = int(input('Entre com um número inteiro: '))
  if n % 2 == 0 : print(f"O número {n} é par!")
  else: print(f"O número {n} é ímpar!")
  continuar = input('Deseja continuar? (Digite s para sim)')
  if continuar != 's': break