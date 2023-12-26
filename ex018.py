from math import sin, cos, tan, radians
angulo = float(input('Digite um ângulo qualquer: '))
r = radians(angulo)
s = sin(r)
c = cos(r)
t = tan(r)
print('O valor de seno é {:.2f}, do cosseno é {:.2f} e tangente é {:.2f}!'.format(s, c, t))
