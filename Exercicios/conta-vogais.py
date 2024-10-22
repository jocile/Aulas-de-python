'''
Crie um programa que leia uma palavra e mostre quantas vogais ela possui.
'''

texto = input('Digite uma palavra: ')
vogais = 0
VOGAIS = 'AEIOU'

for letra in texto:
    if letra in 'aeiou':
        vogais += 1

print(f'A palavra {texto} possui {vogais} vogais')

print("A vogais encontradas são: ")
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end='')
else:
    print('')
