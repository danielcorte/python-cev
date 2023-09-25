def lerarq():
    with open("pessoascadastradas.txt", "r", encoding="utf-8") as arquivo:
        pessoas = arquivo.read()
    print(pessoas)

def criararq():
    with open("pessoascadastradas.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(f"{'Nome':<30}{'Idade':>3}")
        print('O arquivo "pessoascadastradas.txt" foi criado com sucesso.')


def adicioarq(txt):
    with open("pessoascadastradas.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{txt}")


def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f"\033[0;31mERRO! Digite um número inteiro válido.\033[m")
        if ok:
            break
    return valor