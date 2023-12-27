from datetime import date
import time
d_a = date.today().year
ano = int(input('Digite o ano de nascimento: '))
cl = d_a - ano
print('=-'*30)
print('CALCULANDO...')
print('=-'*30)
time.sleep(2)
if cl <= 9:
    atleta = 'MIRIM'
elif 9 < cl <= 14:
    atleta = 'INFANTIL'
elif 14 < cl <= 19:
    atleta = 'JÚNIOR'
elif 19 < cl <= 20:
    atleta = 'SÊNIOR'
else:
    atleta = 'MASTER'
print('O atleta possui {} anos e pertence a categoria {}.'.format(cl, atleta))
