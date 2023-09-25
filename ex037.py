# Exercício Python 037: Escreva um programa em Python que leia um número inteiro
# qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input("Digite um número inteiro: "))
print("Escolha uma das bases para conversão:"
      "[1] converter para BINÁRIO"
      "[2] converter para OCTAL"
      "[3] converter para HEXADECIMAL")
opc = int(input("Qual a sua opção? "))
if opc == 1:
    print(f"{num} convertido para binário é {bin(num[2:])}")
elif opc == 2:
    print(f"{num} convertido para octal é {oct(num[2:])}")
elif opc == 3:
    print(f"{num} convertido para hexadecimal é {hex(num[2:])}")
else:
    print("Opção inválida. Tente novamente!")
