'''num = int(input('Digite um número inteiro: '))
if num//2 == 0:
    print('O número que você digitou é PAR!')
else:
    print('O número que você digitou é IMPAR!')'''
num = int(input('Me diga um número qualquer: '))
resultado = num % 2
if resultado == 0:
    print('O número {} é PAR!'.format(num))
else:
    print('O número {} é IMPAR!'.format(num))
