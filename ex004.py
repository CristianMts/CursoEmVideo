n1 = input('Digite algo: ')
# print(type(n1))
print('{} é numérico e/ou letra?'.format(n1))
print(n1.isalnum())
print('{} é somente letra?'.format(n1))
print(n1.isalpha())
print('{} é somente número?'.format(n1))
print(n1.isnumeric())
print('{} é numérico? '.format(n1), n1.isnumeric())
print('{} está em maiúsculas? '.format(n1), n1.isupper())
print('{} está em minúsculas? '.format(n1), n1.islower())
print('{} está capitalizada? '.format(n1), n1.istitle())
# Resolução
# a = input('Digite algo: ')
# print('O tipo primitivo desse valor é ', type(a))
# print('Só tem espaços? ', a.isspace())
# print('É um número? ', a.isnumeric())
# print('É alfabético? ', a.isalpha())