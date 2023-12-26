lar = float(input('Qual a largura da parede (metros)? '))
alt = float(input('Qual a altura da parede (metros)? '))
a = lar * alt
print('A área total da parede é de {:.2f} m².'.format(a))
print('E serão necessários {:.0f} L de tinta para pintá-la!'.format(a / 2))
# larg = float(input('Largura da parede: '))
# alt = float(input('Altura da parede: '))
# área = larg * alt
# print('Sua parede tem a dimensão de {}x{} e sua área é de {} m².'.format(larg, alt, área))
# tinta = área / 2
# print('Para pintar essa parede, você precisará de {}L de tinta.'.format(tinta))
