d=input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(d))
print('Só tem espaços?', d.isspace())
print('É um número?', d.isnumeric())
print('É alfabetico?', d.isalpha())
print('Está em maiusculo?', d.isupper())
print('Está em minusculas?', d.islower())
print('Está capitalizada?', d.istitle())