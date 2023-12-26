from math import sqrt
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = sqrt(co ** 2 + ca ** 2)
print('O valor da hipotenusa é {:.2f}'.format(hi))
# hi = (co ** 2 + ca ** 2) ** (1/2)
# hi = math.hypot(co, ca)
