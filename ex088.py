# Exercício Python 088: Faça um programa que ajude um jogador
# da MEGA SENA a criar palpites.O programa vai pergunta
# r quantos jogos serão gerados e vai sortear 6 números entre
# 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""from random import randint
from time import sleep
lista = list()
jogos = list()
print("-" * 30)
print("     JOGA NA MEGA SENA     ")
print("-" * 30)
quant = int(input("Quantos jogo você que que eu sorteie? "))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    jogos.clear()
    tot += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f"Jogo {i+1}: {l}")
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)"""
from random import randint
from random import shuffle
megasena = list(range(0,61))
print('-' * 30)
print(f'{"JOGO DA MEGA SENA":^30}')
print('-' * 30)
pergunta = int(input('Quantos números quer que eu sorteie? '))
for aposta in range(1, pergunta+1):
    print(f'Jogo {aposta}: ', end='')
    shuffle(megasena)
    print(megasena[:6])
    del(megasena[:6])
