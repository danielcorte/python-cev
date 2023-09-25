# Exercício Python 044: Elabore um programa que calcule o valor
# a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros
print("==========LOJAS CORTES==========")
preço = float(input("Preço das compras: R$"))
print("FORMAS DE PAGAMENTO\n"
      "[1] à vista dinheiro/cheque\n"
      "[2] à vista cartão\n"
      "[3] 2x no cartão\n"
      "[4] 3x ou mais no cartão")
opção = int(input("Qual é a opção? "))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print(f"A compra será parcelada em 2x de R${parcela:.2f}")
elif opção == 4:
    parcela = int(input("Em quantas vezes deseja parcelar? "))
    total = preço + (preço * 20 / 100)
    vf = total / parcela
    print(f"A compra será parcelada em {parcela}x de R${vf:.2f}")
print(f"Sua compra de R${preço:.2f} vai custar R${total:.2f} no final.")