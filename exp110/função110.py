def resumo(num, juros=0, descont=0):
    dobro = num * 2
    metade = num / 2
    j = num + (num / 100 * juros)
    d = num - (num / 100 * descont)
    print("-" * 30)
    print("RESUMO DO VALOR".center(30))
    print("-" * 30)
    print(f"Preço analisado: \tR${num}".replace(".", ","))
    print(f"Dobro do preço: \tR${dobro}".replace(".", ","))
    print(f"Metade do preço: \tR${metade}".replace(".", ","))
    print(f"Com {juros}% de juros: \tR${j}".replace(".", ","))
    print(f"Com {descont}% de baixa: \tR${d}".replace(".", ","))
    print("-" * 30)
