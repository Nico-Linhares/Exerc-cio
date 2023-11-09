'Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente'

import math
angulo = float(input('Digite o angulo que vc deseja: '))
seno = math.sin(math.radians(angulo))
print('O angulo de {} tem o seno {:.2f}'.format(angulo, seno))
coseno = math.cos(math.radians(angulo))
print('O angulo {} tem cosseno {:.2f}'.format(angulo, coseno))
tangente = math.tan(math.radians(angulo))
print ('O angulo de {} tem a tangente {:.2f}'.format(angulo, tangente))
print('>'*200)

'Uma forma mais simplificada'

from math import sin, cos, tan, radians
an = float(input('Digite um ângulo: '))
se = sin(radians(an))
co = cos(radians(an))
ta = tan(radians(an))
print('O ângulo {} tem como seno {:.2f}, cosseno {:.2f} e tangete {:.2f}'.format(an, se, co, ta))


