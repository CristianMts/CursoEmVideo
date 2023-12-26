#nome = input('Digite seu nome completo: \n')
#print('Seu primeiro nome é {}!'.format(nome.split()[0]))
'''Ao soliticar split(), a leitura é da direita para esquerda, iniciando no ZERO 0
Quando quero iniciar da esquerda para direita'''
#print('Sey primeiro nome é {}!'.format(nome.split()[-4]))
#print('O seu último nome é {}!'.format(nome.split()[-1]))

n = str(input('Digte seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
# Abaixo, segue meu código revisado:

name = str(input('Digite seu nome completo: ')).strip()
print('Muito prazer em te conhecer {}'.format(name))
print('Seu primeiro nome é {}!'.format(name.split()[0]))
print('Seu último nome é {}!'.format(name.split()[-1]))
