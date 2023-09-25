casa = float(input("Valor da casa: R$"))
salario = float(input("Salário do comprador: R$"))
anos = int(input("Em quantos anos será o financiamento: "))
prest = casa / (anos * 12)
mini = salario * 30 / 100
print(f"Para pagar uma casa de R${casa:.2f} em {anos}")
print(f"A prestação da casa será de R${prest}")
if prest <= mini:
    print(f"Empréstimo PODE ser concedido!")
else:
    print(f"Empréstimo NEGADO!")
