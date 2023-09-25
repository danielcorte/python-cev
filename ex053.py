# Exercício Python 053: Crie um programa que leia uma frase
# qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
#
# Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA,
# A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
frase = str(input("Digite uma frase: ").upper().strip())
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''
print(f"O inverso de {junto} é {inverso}")
if inverso == junto:
    print("TEMOS um palíndromo")
else:
    print("A frase digitada NÃO É um palíndromo")
