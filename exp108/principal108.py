from exp108 import função108
valor = float(input("Digite o preço: R$"))
print(f"A metade de R${valor:.2f} é {função108.moeda(função108.metade(valor))}")
print(f"O dobro de R${valor:.2f} é {função108.moeda(função108.dobro(valor))}")
print(f"Com 10% de juros, {função108.moeda(função108.juros(valor))}")
print(f"Com 13% de desconto, {função108.moeda(função108.desconto(valor))}")
