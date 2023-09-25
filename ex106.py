# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help
# do Python. O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
from time import sleep


def interactivehelp(func):
    print('\033[34m~' * (len(func) + 31))
    print(f"Acessando o manual do comando {func}")
    print('\033[34m~\033[m' * (len(func) + 31))
    print("\033[1;30;46m")
    sleep(1)
    print(f"{help(func)}")
    print("\033[m")


while True:
    print("\033[1;34m=" * 24)
    print("SISTEMA DE AJUDA PYHELP")
    print("========================\033[m")
    question = str(input("\033[1;34mFunção ou Biblioteca > \033[m"))
    if question == "fim":
        break
    interactivehelp(question)
print("\033[1;36m=========")
print("ATÉ LOGO")
print("=========\033[m")

 