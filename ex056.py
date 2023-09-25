# Exercício Python 056: Desenvolva um programa que leia o nome,
# idade e sexo de 4 pessoas. No final do programa, mostre: a
# média de idade do grupo, qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.
somaidade = mediaidade = maioridadehomem = totmulher20 = 0
nomevelho = ''
for p in range(1, 5):
    print(f"----- {p}° PESSOA -----")
    nome = str(input("Nome: ").strip())
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]:").upper().strip())
    somaidade += idade
    if p == 1 and sexo in "M":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "M" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "F" and idade < 20:
        totmulher20 += 1
mediaidade = mediaidade / 4
print(f"A média de idade do grupo é {mediaidade} anos")
print(f"O nome do homem mais velho é {nomevelho}")
print(f"Ao todo são {totmulher20} mulheres com menos de 20 anos")
