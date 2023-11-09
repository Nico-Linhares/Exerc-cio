

velocidade = float(input('Qual a sua velocidade? '))
if velocidade > 80:
    print ('Você está acima do velocidade aceitavel')
    multa = (velocidade - 80) * 7
    print ('Sua multa é de {:.2f}'.format(multa))
else:
    print ('Muito bem, você estar dentro do limite')








