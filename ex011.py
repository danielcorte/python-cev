# Exercício Python 011: Faça um programa que leia a largura e a altura
# de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
larg = float(input("Largura da parede: "))
altu = float(input("Altura da parede: "))
area = larg * altu
print(f"Sua parede tem dimensão de {larg}x{altu} e a sua área é de {area}m²")

