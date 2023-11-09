'Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome santos'

c = str(input('Qual cidade vc nasceu? ')).strip()
print (c[:5].upper() == 'SANTO')


cid = str(input('Qual sua cidade nata? ')).strip()
print(cid[:6].upper() == 'BURITI')
