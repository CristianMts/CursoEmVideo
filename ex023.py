#num = str(input('Digite um número de 0 a 9999: '))
#print('Unidade: ', num[3])
#print('Dezena: ', num[2])
#print('Centena: ', num[1])
#print('Milhar: ', num[0])
'''Um erro acontece no meu programa. Digitanto um número de 4 ou mais caracteres, funciona, porém
ao digitar 1 ou 11 ou 111, não há números para impressão'''
#Método matemárico:
num = int(input('Digite um número de 0 a 9999: '))
u = num % 10
d = (num // 10) % 10
c = (num // 100) % 10
m = (num // 1000 )
print("A(s) unidade(s) de {} é {}!\nA(s) Dezena(s): {}!\nCentena(s): {}! \nMilhar(es): {}!".format(num, u, d, c, m))
