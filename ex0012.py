'crie um programa que leia o nome de uma pessoa e diga se ela tem Silva no nome'

nome = str(input('Digite de seu nome completo: ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
