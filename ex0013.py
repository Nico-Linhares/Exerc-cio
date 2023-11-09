'faça um programa que leia uma frase pelo teclado e mostre'
#quantas vezes aparece a letra a
#em que posição ela aparece a primeira vez
#em que posião ela aparece a ultima vez

frase = str(input('Digite uma frase: ')).strip()
print ('a letra A aparece {} vezes'.format(frase.count('a')))
print ('A letra A tem sua primeira posição {}'.format(frase.find('a')+1))
print ('a letra a aparece pela ultima vez na posião {}'.format(frase.rfind('a')+1))

