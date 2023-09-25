# Exercício Python 089: Crie um programa que leia nome e duas
# notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e
# permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""ficha = list()
while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([[nome], [nota1], [nota2], media])
    resp = str(input("Deseja continuar? [S/N]: ").strip().upper())
    if resp in "N":
        break
print("-=" * 30)
print(f"{'No.':<4}{'NOME':<10}{'Média':>8}")
print("-" * 26)
for i, a in enumerate(ficha):
    print(f"{i:<4}{a[0]:>10}{a[2]:>8.1f}")
while True:
    print('-' * 35)
    opc = int(input("Mostrar notas de qual aluno? (999 para parar): "))
    if opc == 999:
        break
    if opc <= len(ficha) -1:
        print(f"Notas de {ficha[opc][0]} são {ficha[opc][1]}")
print("<<< VOLTE SEMPRE >>>")"""
from time import sleep
lista = []
cont = 0
contreprovados = 0
contaprovados = 0
contrecuperados = 0
while True:
    nome = str(input('\033[1;37mNome: ')).strip().capitalize()
    nota1 = float(input('\033[1;33m1ª Nota: '))
    nota2 = float(input('2ª Nota: '))
    nota3 = float(input('3ª Nota: '))
    nota4 = float(input('4ª Nota: \033[m'))
    media = (nota2 + nota1 + nota4 + nota3) / 4
    print('=-' * 30)
    lista.append([nome, [nota1, nota2, nota3, nota4], media])
    res = str(input('Deseja continuar? \033[1;36m[ S / N ]\033[1;36m ')).strip().upper()[0]
    while res not in 'SN':
        print('\033[1;31mPOR FAVOR! \033[1;34mDigite uma opção válida...\033[m')
        res = str(input('Deseja continuar? \033[1;36m[ S / N ] \033[m')).strip().upper()[0]
    if res in 'S':
        print('\033[1;34mOK! Vamos prosseguir...\033[m')
        print('=-' * 30)
        sleep(1)
    if res in 'N':
        print('\033[1;34mOK! Encerrando o programa...\033[m')
        print('=-' * 30)
        sleep(1.5)
        break
print(f'\033[1;32m{"Nº":<4}\033[1;34m{"NOME":<6}\033[1;33m{"MÉDIA":>8}\033[m')
print('-' * 19)
for i, a in enumerate(lista):
    print(f'{i:<4}\033[1;36m{a[0]:<6}\033[1;31m{a[2]:>7.1f}\033[m')
print('=-' * 30)
sleep(1)
while True:
    notas = int(input('Deseja mostrar as notas de qual aluno? \033[1;36m(999 interrompe)\033[m '))
    print('--' * 30)
    sleep(1.2)
    if notas == 999:
        print('--' * 30)
        break
    if notas <= len(lista) - 1:
        print(f'As notas de \033[1;36m{lista[notas][0]}\033[m são: \033[1;31m{lista[notas][1]}\033[m')
        cont += 1
        print('--' * 30)
        if lista[notas][2] >= 6.5:
            print(f'\033[1;36m{lista[notas][0]}\033[m está \033[1;34mAPROVADO!\033[m')
            contaprovados += 1
            print('--' * 30)
        elif 4 <= lista[notas][2] < 6.5:
            print(f'\033[1;36m{lista[notas][0]}\033[m está de \033[1;33mRECUPERAÇÂO!\033[m')
            contrecuperados += 1
            print('--' * 30)
        else:
            print(f'\033[1;36m{lista[notas][0]}\033[m está \033[1;31mREPROVADO!\033[m')
            contreprovados += 1
            print('--' * 30)
        sleep(1.5)
    if cont == len(lista):
        print('\033[1;32mA nota de todos alunos já foram exibidas!\033[m')
        print('--' * 30)
        sleep(1.3)
        break
print(f'Há \033[1;31m{len(lista)} alunos\033[m nesta turma.')
print('--' * 30)
if contaprovados == 0:
    print('\033[1;31mNenhum aluno foi aprovado.\033[m')
else:
    print(f'\033[1;31m{contaprovados} aluno{"s" if contaprovados > 1 else ""}\033[m foram aprovados.')
if contrecuperados == 0:
    print('\033[1;31mNehnhum aluno ficou de recuperação.\033[m')
else:
    print(f'\033[1;31m{contrecuperados} aluno{"s" if contrecuperados > 1 else ""}\033[m ficaram de recuperação.')
if contreprovados == 0:
    print('\033[1;31mNenhum aluno foi reprovado.\033[m')
else:
    print(f'\033[1;31m{contreprovados} aluno{"s" if contreprovados > 1 else ""}\033[m foram reprovados.')
print('--' * 30)
print('\033[1;34mPROGRAMA ENCERRADO!')