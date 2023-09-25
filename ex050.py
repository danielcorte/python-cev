# Exercício Python 050: Desenvolva um programa que leia seis números
# inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = cont = 0
for c in range(1, 7):
    num = int(input(f"Digite o {c} valor: "))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f"Você informou {cont} valores pares e a soma foi {soma}")