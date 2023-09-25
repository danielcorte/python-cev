# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
itens = ["pedra", "papel", "tesoura"]
computador = randint(0, 2)
print("Suas opções: \n"
      "[1] pedra\n"
      "[2] papel\n"
      "[3] tesoura")
jogador = int(input("Qual é a sua jogada? "))
print("JO!!")
sleep(1)
print("KEN!!")
sleep(1)
print("PO!!")
sleep(1)
print("=" * 20)
print(f"Computador jogou {itens[computador]}")
print(f"Jogador jogou {itens[jogador]}")
print("=" * 20)
if computador == 0:  # Computador jogou PEDRA
    if jogador == 0:
        print("EMPATE")
    if jogador == 1:
        print("JOGADOR VENCE")
    if jogador == 2:
        print("COMPUTADOR VENCE")
elif computador == 1:  # Computador jogou PAPEL
    if jogador == 0:
        print("COMPUTADOR VENCE")
    if jogador == 1:
        print("EMPATE")
    if jogador == 2:
        print("JOGADOR VENCE")
elif computador == 2:  # Computador jogou TESOURA
    if jogador == 0:
        print("JOGADOR VENCE")
    if jogador == 1:
        print("JOGADOR PERDE")
    if jogador == 2:
        print("EMPATE")