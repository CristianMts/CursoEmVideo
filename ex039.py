from datetime import date
data_atual = date.today()
nasc = int(input("Digite o Ano do Seu Nascimento: "))
idade = data_atual.year - nasc
if idade < 18:
    tempo = 18 - idade
    print("Você ainda vai se alistar ao serviço Militar. Falta(m) {} ano(s).".format(tempo))
elif idade == 18:
    print("É a hora de você se alistar ao serviço Militar. Você completa(ou) 18 anos em {}.".format(data_atual.year))
else:
    tempo = idade - 18
    print("Já passou o tempo de alistamento para você. Se passou {} anos.".format(tempo))