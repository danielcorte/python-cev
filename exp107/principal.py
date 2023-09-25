import funções
valor = float(input("Digite o preço: R$"))
print(f"A metade de R${valor:.2f} é R${funções.metade(valor):.2f}")
print(f"O dobro de R${valor:.2f} é R${funções.dobro(valor):.2f}")
print(f"Com 10% de juros, R${funções.juros(valor):.2f}")
