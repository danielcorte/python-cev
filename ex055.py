# Exercício Python 055: Faça um programa que leia o peso de
# cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = menor = 0
for p in range(1, 6):
    peso = float(input(f"Qual o peso da {p}° pessoas: "))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f"O maior peso registrado foi {maior}Kg")
print(f"O menor peso registrado foi {menor}Kg")
