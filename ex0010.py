'Faça um programa que leia um numero de 0 a 9999 e monstre na tela cada um dos digitos separados'
'ex unidade, dezenas, centenas, milhar'

n = int(input('Digite um valor entre 0 a 9999: '))
unidade = n // 1 % 10
dezenas = n // 10 % 10
centenas = n // 100 % 10
milhar = n // 1000 % 10
print ('Analisando o número... ')
print ('Unidade {}'.format(unidade))
print ('Dezenas {}'.format(dezenas))
print ('Centenas {}'.format(centenas))
print ('Milhar {}'.format(milhar))

#com isso foi possivel fatiar o numero



