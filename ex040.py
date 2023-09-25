# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
med = (n1 + n2) / 2
print(f"Tirando notas {n1:.1f} e {n2:.1f} a média do aluno será {med}")
if 7 > med >= 5:
    print("O aluno está de RECUPERAÇÃO!")
elif med < 5:
    print("O aluno está REPROVADO!")
elif med > 7:
    print("O aluno está APROVADO!")
