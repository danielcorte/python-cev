# Exercício Python 043: Desenvolva uma lógica que leia o peso e
# a altura de uma pessoa, calcule seu Índice de Massa Corporal
# (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida
peso = float(input("Qual é o seu peso? (KG)"))
altura = float(input("Qual é a sua altura? (m)"))
imc = peso / (altura ** 2)
print(f"O IMC dessa pessoa é {imc}")
if imc <= 18.5:
    print("Você está ABAIXO do peso")
elif imc <= 18.5 < 25:
    print("Você está no peso IDEAL")
elif imc <= 25 < 30:
    print("Você está com SOBREPESO")
elif imc <= 30 < 40:
    print("Você está com OBESIDADE")
elif imc > 40:
    print("Você está com OBESIDADE MÓRBIDA")
