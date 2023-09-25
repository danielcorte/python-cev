# Exercício Python 109: Modifique as funções que form criadas no desafio 107
# para que elas aceitem um parâmetro a mais, informando se o valor retornado
# por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

from exp109 import função109
valor = float(input("Digite o preço: R$"))
print(f"A metade de R${valor} é {função109.metade(valor, formata=True)}")
print(f"O dobro de R${valor} é {função109.dobro(valor, formata=True)}")
print(f"Aumentando 30%, é {função109.aumentar(valor, 30, formata=True)}")
print(f"Diminuindo 25%, é {função109.diminuir(valor, 25, formata=True)}")
