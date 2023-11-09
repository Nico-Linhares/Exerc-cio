n=input('Digite seu nome: ')
print('Olá {}!, seja bem-vindo!'.format(n))
print('-'*200)


no=input('Digite seu nome: ')
print('seja bem-vindo {:20}!'.format(no))
print('-'*200)

nom=input('Digite seu nome: ')
print('seja bem-vindo {:>20}!'.format(nom))
print('-'*200)

nome=input('Digite seu nome: ')
print('Seja bem-vindo {:^20}!'.format(nome))
print('-'*200)

v=int(input('Valor: '))
v2=int(input('Valor: '))
s=v + v2
sub=v - v2
m=v * v2
d=v / v2
di=v ** v2
e=v // v2
print('Os valores {} e {} tem como soma: {}, subtração: {}, multiplicação: {}, divisão: {}, divisão inteira: {:.3f} e exponenciação: {:.3f}'.format(v, v2, s, sub, m, d, di, e))
print('-'*200)

v3=int(input('Valor: '))
v4=int(input('Valor: '))
so=v3 + v4
subt=v3 - v4
mu=v3 * v4
div=v3 / v4
divi=v3 ** v4
ex=v3 // v4
print('Os valores {} e {} tem como soma {}, subtra {}, multi {}, divi {}'.format(v3, v4, so, subt, mu, div))
print('divi inte {}, exp {}'.format(divi, ex))
print ('-'*200)

v5=int(input('Valor: '))
v6=int(input('Valor: '))
soma = v5 + v6
subtra = v5 - v6
multipli = v5 * v6
divisao = v5 / v6
diviintei = v5 ** v6
exponen = v5 // v6
print('Os valores de {} e {} somados {}, diminuidos {}, multiplicados {}, divididos {}'.format(v5, v6, soma, subtra, multipli, divisao), end=' ')
print('divisão intei {} e exponeci {}'.format(diviintei, exponen))
print('-'*200)

v7=int(input('valor: '))
v8=int(input('valor: '))
somm = v7 + v8
subb = v7 - v8
muu = v7 * v8
dii = v7 / v8
diii = v7 ** v8
exx = v7 // v8
print('Os valor {} e o {}, \n somados {}, \n diminuidos {}, \n multiplicados {}, \n divididos {}, \n divi indire {}, \n exponeciação {}'.format(v7, v8, somm, subb, muu, dii, diii, exx))
print('-'*200)
