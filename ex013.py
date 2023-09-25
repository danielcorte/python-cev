# Exercício Python 013: Faça um algoritmo que leia o salário de um
# funcionário e mostre seu novo salário, com 15% de aumento.
s = float(input("Qual é o salário do funcionário? R$"))
a = s + (s * 15 / 100)
print(f"Um funcionário que ganhava R${s:.2f}, com 15% de aumento, passará a receber R${a:.2f}")
