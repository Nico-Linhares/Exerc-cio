'Faça um programa que leia o dos quatro alunos e mostre a ordem sorteada'

import random
a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem será: {}'.format(lista))

'a palavra shuffle significa embaralhar'


import random
aa1 = str(input('Nome 1: '))
aa2 = str(input('Nome 2: '))
aa3 = str(input('Nome 3: '))
aa4 = str(input('Nome 4: '))
aa5 = str(input('Nome 5: '))
lista2 = [aa1, aa2, aa3, aa4, aa5]
random.shuffle(lista2)
print ('A ordem')