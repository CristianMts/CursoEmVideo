num = int(input("Digite um número que deseja converter: "))
print("Escolha a seguir, a opção par qual deseja converter \n[1] para binário \n[2] para octal \n[3] para hexadecimal")
opcao = int(input("Opção: "))
if opcao == 1:
    numero = str(bin(num))
    nome = str("binário")
elif opcao == 2:
    numero = str(oct(num))
    nome = str("octal")
else:
    numero = str(hex(num))
    nome = str("hexadecimal")
print("O número {} em {} é {}.".format(num, nome, numero[2:]))