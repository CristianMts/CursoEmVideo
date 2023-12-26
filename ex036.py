casa = (float(input('Digite o valor da Casa a ser financiado: R$ ')))
salario = (float(input('Digite o valor da renda bruta: R$ ')))
anos = (int(input('Em quantos anos deseja parcelar o imóvel? ')))
financiamento = casa / (anos*12)
renda = salario * 0.3
if renda >= financiamento:
    print("-+"*35)
    print("PARABÉNS! :) \nSeu financiamento foi pré-aprovado!!!")
    print("Seu imóvel de R$ {:.2f}, será parcelado em {}x de R$ {:.2f}".format(casa,anos*12,financiamento))
    print("-+"*30)
else:
    print("-+"*35)
    print("QUE PENA! :( \nSeu financimento não foi aprovado!")
    print("-+"*35)
