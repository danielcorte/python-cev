# Exercício Python 035: Desenvolva um programa que leia o comprimento
# de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('=-' * 15)
print(" ANALISADOR DE TRIÃNGULOS ")
print('=-' * 15)
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f"Os segmentos acima PODEM formar um triângulo!")
else:
    print(f"Os segmentos aciam NÃO PODEM formar um triângulo!")
