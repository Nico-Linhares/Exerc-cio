'Faça um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e o ultimo nome '

n = str(input('Qual seu nome completo: ')).strip().capitalize()
nome = n.split()
print ('Seu primeiro nome {}'.format(nome[0]))
print ('Seu ultimo nome é {}'.format(nome[len(nome)-1]))




#o split é diferente o strip, o primeiro vai como se fosse fatiar todo o nome




