# Exercício Python 008: Escreva um programa que leia um
# valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input("Digite uma distância em metros: "))
cent = m * 100
mili = m * 1000
print(f"A medida de {m}M corresponde a {cent}Cm e {mili}Mm")
