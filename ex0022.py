a = int(input('valor 1: '))
b = int(input('Valor 2: '))
c = int(input('Valor 3: '))
manor = a
if b < a and b < c:
    manor = b
if c < a and c < b:
    manor = c
print('O manor valor é {}'.format(manor))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor é {}'.format(maior))



