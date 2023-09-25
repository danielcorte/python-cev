def metade(num, formata=False):
    """

    :param num: o número a ser manipulado
    :param formata: transforma o num em dinheiro
    :return: retorna o que foi pedido
    """
    if formata:
        return f"R${num / 2:>.2f}".replace(".", ",")


def dobro(num, formata=False):
    """

    :param num: o número a ser manipulado
    :param formata: transforma o num em dinheiro
    :return: retorna o valor pedido
    """
    if formata:
        return f"R${num * 2:>.2f}".replace(".", ",")


def aumentar(num, porcentagem=0, formata=False):
    """

    :param num: o número a ser manipulado
    :param porcentagem: a quantidade de juros
    :param formata: transforma o num em dinheiro
    :return: retorna o que foi pedido
    """
    f = num + (num / 100 * porcentagem)
    if formata:
        return f"R${f:>.2f}".replace(".", ",")


def diminuir(num, porcentagem=0, formata=False):
    """

        :param num: o número a ser manipulado
        :param porcentagem: a quantidade de desconto
        :param formata: transforma o num em dinheiro
        :return: retorna o que foi pedido
        """
    f = num - (num / 100 * porcentagem)
    if formata:
        return f"R${f:>.2f}".replace(".", ",")


def resumo(num=0, taxa=15, desc=10):
    print("-" * 30)
    print("RESUMO DO VALOR".center(30))
    print("-" * 30)
    print(f"Preço analisado: \tR${num}")
    print(f"Dobro do preço: \tR${dobro(num, formata=True)}")
    print(f"Metade do preço: \tR${metade(num, formata=True)}")
    print(f"Com {taxa}% de juros: \tR${aumentar(num, taxa, formata=True)}")
    print(f"Com {desc}% de baixa: \tR${diminuir(num, desc, formata=True)}")
    print("-" * 30)

