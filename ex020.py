from random import shuffle

a1 = input('Digite o nome do Aluno 1: ')
a2 = input('Digite o nome do Aluno 2: ')
a3 = input('Digite o nome do Aluno 3: ')
a4 = input('Digite o nome do Aluno 4: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação será assim:\n{}'.format(', '.join(lista)))
# n1 = str(input('Primeiro aluno: '))
# n2 = str(input('Segundo aluno: '))
# n3 = str(input('Terceiro aluno: '))
# n4 = str(input('Quarto aluno: '))
# lista = [n1, n2, n3, n4]
# random.shuffle(lista)
# print('A ordem de apresentação será ')
# print(lista)
