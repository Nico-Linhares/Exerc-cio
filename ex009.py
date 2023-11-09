'Crie um programa que leia o nome completo de uma pessoa e mostre:'
#O nome com todas as letra maiusculas e minusculas
#Quantas letras ao todo sem contar os espaços
#quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome... ')
print('Seu nome em maiusculas é: {}'.format(nome.upper()))
print('Seu nome em minusculas é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome {} tem {} letras'.format(separa[0], len(separa[0])))





#a palavra 'strip' traduzida é faixa, ela serve para eliminar os espaços
#pq usar somente o upper e lower e não isupper e islower ? pq usando o 'is' o programa vai entender q estou perguntando se é vdd ou nao
#o format.(len(nome) - nome.count(' '))) serve para contar as letras sem os espaço entre os nomes
#











