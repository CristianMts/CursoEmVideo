'''nome = str(input('Digite seu nome completo: '))
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(" "))
print(len(nome ))'''

nome_completo = input('Digite o seu nome completo: ')
print('Nome em maiúsculas:', nome_completo.upper())
print('Nome em minúsculas:', nome_completo.lower())
num_letras = len(nome_completo.replace(' ', ''))
print('Total de letras:', num_letras)
primeiro_nome = nome_completo.split()[0]
num_letras_primeiro_nome = len(primeiro_nome)
print('Número de letras do primeiro nome:', num_letras_primeiro_nome)

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome..')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
