n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2
if m < 5.0:
    print('Você foi Reprovado! Sua nota final é {:.1f}'.format(m))
elif 5.0 <= m <= 6.9:
    print('Você está em Recuperação! Sua nota final é {:.2f}'.format(m))
else:
    print('Você foi Aprovado! Sua nota final é {:.1f}'.format(m))
