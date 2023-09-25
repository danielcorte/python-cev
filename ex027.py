# Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza (primeiro = Ana; último = Souza.
n = str(input("Digite seu nome completo: ")).strip()
nome = n.split()
print("Muito prazer em te conhecer!")
print(f"Seu primeiro nome é {nome[0]}")
print(f"Seu último nome é {len(nome[-1])}")

