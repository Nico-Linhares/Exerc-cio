n=int(input('Digite um valor: '))
s = n + 1
d = n - 1
print('O valor {} tem como seu posterior {} e seu antecessor {}'.format(n, s, d))
print('>'*100)

nu=int(input('Digite um valor: '))
dobro = nu * 2
triplo = nu * 3
raiz = nu ** (1/2)
print('O valor {} tem como dobro {}, triplo {} e raiz {:.3f}'.format(nu, dobro, triplo, raiz))
print('>'*100)

nota1=float(input('Nota 1: '))
nota2=float(input('Nota 2: '))
soo = (nota1 + nota1) / 2
print('As notas do aluno é {} e {} e tem media  {}'.format(nota1, nota2, soo))
print('>'*100)

med=float(input('Digite uma medida: '))
cen = med * 100
mil = med * 1000
print('A medida {} tem {:.3f} centimetro e {:.3f} milimetros'.format(med, cen, mil))
print('>'*100)

tab=int(input('Digite um valor'))
v0 = tab + 0
v1 = tab + 1
v2 = tab + 2
v3 = tab + 3
v4 = tab + 4
v5 = tab + 5
v6 = tab + 6
v7 = tab + 7
v8 = tab + 8
v9 = tab + 9
v10 = tab + 10
print('A tadua de {:2} é: \n {:2} + 0 = {:2} \n {:2} + 1 = {:2} \n {:2} + 2 = {:2} \n {:2} + 3 = {:2} \n {:2} + 4 = {:2} \n {:2} + 5 = {:2} \n {:2} + 6 = {:2} \n {:2} + 7 = {:2} \n {:2} + 8 = {:2} \n {:2} + 9 = {:2} \n {:2} + 10 = {:2}'.format(tab, tab, v0, tab, v1, tab, v2, tab, v3, tab, v4, tab, v5, tab, v6, tab, v7, tab, v8, tab, v9, tab, v10))
print('>'*100)


real=float(input('Quanto dinheiro vc tem na carteira: R$ '))
dolar = real / 5.24
euro = real / 5.55
iene = real / 0.038
print('Com a quantidade {} de R$ em dolares fica {:.2f}, em euro {:.2f} e em iene {:.2f}'. format(real, dolar, euro, iene))

print('>'*100)

larg = float(input('Qual a largura da parade: '))
alt = float(input('Qual a altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua area de {}m²'.format(larg, alt, area))
tinta = area / 8
print('Para pintar essa parede será preciso de {}l de tinta'.format(tinta))

print('>'*100)

des = float(input('Preço do Produto: '))
desc = des - (des * 5 / 100)
print('O produto que custa {} com 5% de desconto fica {}'.format(des, desc))

print('>'*100)

aum=float(input('Qual o salario atual do funcionario ? '))
aume= aum + (aum * 15 / 100)
print('O salario dele era {} mas com 15% de aumento ficou {}'.format(aum, aume))

print('>'*100)

c = float(input('Informe sua temperatura em Cº '))
f = ((9*c) / 5) + 32
print('A temperatuda {}Cº corresponde a {}Fº'.format(c, f))

print('>'*100)

km = float(input('Qual km foram percorridos: '))
dias = float(input(('Quantos dias ficou alugado: ')))
aa = (km * 0.15) + (dias * 60)
print ('O total a pagar é {}R$'.format(aa))


