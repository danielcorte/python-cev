# Exercício Python 051: Desenvolva um programa que leia o primeiro termo
# e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decim = termo + (10 - 1) * razao
for c in range(termo, decim + razao, razao):
    print(f"{c}", end="-> ")
print("ACABOU!!")