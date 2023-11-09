'Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo os nomes e mostrando qual será escolhido'

import random
n1 = input('Alono 1: ')
n2 = input('Aluno 2: ')
n3 = input('Aluno 3: ')
n4 = input('Aluno 4: ')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhi foi {}'.format(escolhido))
