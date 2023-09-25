# Exercício Python 012: Faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço, com 5% de desconto.
p = float(input("Informe o preço do produto: R$"))
d = p + (p / 100 * 5)
print(f"O produto que custava R${p}, na promoção com desconto de 5% vai custar R${d}")
