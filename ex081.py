# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
valores = []
while True:
    valores.append(int(input("Digite um valor: ")))
    resp = str(input("Deseja continuar? [S/N]: ").upper().strip()[0])
    if resp in 'N':
        break
print("-=" * 30)
print(f"Você digitou {len(valores)} elementos.")
valores.sort(reverse=True)
print(f"Os valores em ordem decrescente são {valores}")
if 5 in valores:
    print("O valor 5 FAZ parte da lista")
else:
    print("O valor 5 NÃO faz parte da lista")
