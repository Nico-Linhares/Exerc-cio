'Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo. Calcule e mostre o comprimento da hipotenusa.'

co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print ('A hipotenusa vai medir {:.2f}'.format(hi))

'Tem outra maneira de fazer esse calculo usando a biblioteca math'

import math
cop = float(input('Cateto oposto: '))
cad = float(input('Cateto adjacente: '))
hip = math.hypot(cop, cad)
print('A hipotenusa vai medir {:.2f}'.format(hip))
 