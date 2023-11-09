'Escreva um programa que faça o pc pensar em um número inteiro de 0 a 5 e peça para o usuario tentar descobrir'
'qual foi o numero escolhido pelo pc. O programa deverá mostrar a tela se o usuario perdeu ou ganhou'

from random import randint

pc = randint(0, 5) #faz o pc pensar
print('Vou pensar em número. Tente acertar...')
usu = int(input('Digite um número entre 0 a 5: '))
if usu == pc:
    print ('Parabéns vc acertou :) ')
else:
    print('Não foi dessa vez')  





