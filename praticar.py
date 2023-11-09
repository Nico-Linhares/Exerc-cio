a = int(input('Digite um valor: '))
b = int(input('Digite um valor: '))
c = int(input('Digite um valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor valor é {}'.format(menor))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('o maior valor é {}'.format(maior))
























