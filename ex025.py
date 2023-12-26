#nome = input('Escreva seu nome: ')
#nomeT = nome.title()
#print('O seu nome contém "Silva"? ', 'Silva' in nomeT)

name = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('Silva' in name.title()))
