# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.
nome = str(input("Digite o seu nome: "))
print(f"O seu nome em maiúsculas é {nome.upper()}")
print(f"O seu nome em minúsculas é {nome.lower()}")
print(f"Ao todo o seu nome tem {len(nome)} letras")
