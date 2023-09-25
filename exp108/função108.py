def metade(num):
    f = num / 2
    return f


def dobro(num):
    f = num * 2
    return f


def juros(num):
    f = num * 1.10
    return f


def desconto(num):
    f = num * 0.87
    return f


def moeda(preço=0, moeda="R$"):
    return f"{moeda}{preço:>.2f}".replace(".", ",")