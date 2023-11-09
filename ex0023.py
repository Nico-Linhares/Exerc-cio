'Faça um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento'
'Para salários superiores a 1250,000, calcule um aumento de 10%'
'para inferiores ou igual, o aumento é até 15%'

salario = float(input('Qual o seu salário? '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(' Seu salário que era {} agora é {}'.format(salario, novo))





