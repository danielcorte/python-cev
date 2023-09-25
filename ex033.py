# Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))
# Verificando quem é menor
menor = a
if b < a:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é menor
maior = a
if b > a:
    maior = b
if c > a and c > b:
    maior = c
print(f"O maior valor digitado foi {maior}")
print(f"O menor valor digitado foi {menor}")
