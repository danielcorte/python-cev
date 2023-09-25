# Exercício Python 010: Crie um programa que leia quanto dinheiro
# uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
d = float(input("Quanto dinheiro você tem na carteira? R$ "))
dolar = d / 5
print(f"Com R${d:.2f} você pode comprar U${dolar:.2f}")
