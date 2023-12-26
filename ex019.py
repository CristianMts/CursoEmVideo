import random

a1 = input('Digite o nome do Aluno 1: ')
a2 = input('Digite o nome do Aluno 2: ')
a3 = input('Digite o nome do Aluno 3: ')
a4 = input('Digite o nome do Aluno 4: ')
lista = [a1, a2, a3, a4]
sorteio = random.choice(lista)
print('O aluno sorteado foi {}!'.format(sorteio))
# n1 = str(input('Primeiro aluno: '))
# n2 = str(input('Segundo aluno: '))
# n3 = str(input('Terceiro aluno: '))
# n4 = str(input('Quarto aluno: '))
# lista = [n1, n2, n3, n4]
# escolhido = random.choice(lista)
# print('O aluno escolhido foi {}'.format(escolhido))

# lista = input('Digite o nome do Aluno 1: '), input('Digite o nome do Aluno 2: '), ....
