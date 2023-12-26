#cidade = input('Digite o nome da sua cidade: ')
#p_cidade = cidade.split()[0]
#c_cidade = p_cidade.upper()
#print('É verdade que o primeiro nome de sua cidade é Santo? ')
#print('SANTO' in c_cidade)

cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')
