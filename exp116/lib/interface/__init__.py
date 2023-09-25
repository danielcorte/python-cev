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


def linha(tam=0):
    return "-" * tam


def cabecalho(txt):
    print(linha(40))
    print(txt.center(40))
    print(linha(40))


def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"\033[33m{c} -\033[m \033[34m{item}\033[m")
        c += 1
    print(linha(40))
    opc = leiaint("\033[32mSua Opção: \033[m")
    return opc
