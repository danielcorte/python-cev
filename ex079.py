# Exercício Python 079: Crie um programa onde o usuário possa digitar
# vários valores numéricos e cadastre-os em uma lista. Caso o número
# já exista lá dentro, ele não será adicionado. No final, serão
# exibidos todos os valores únicos digitados, em ordem crescente.
numeros = list()
while True:
    n = int(input("Digite um número: "))
    if n not in numeros:
        numeros.append(n)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado! Não vou adicionar...")
    r = str(input("Quer continuar? [S/N]: ").strip())
    if r in "Nn":
        break
print("~" * 30)
numeros.sort()
print(f"Você digitou os valores {numeros}")
