from exp115 import arquivos
while True:
    print("-" * 40)
    print("MENU PRINCIPAL".center(40))
    print("-" * 40)
    print("\033[0;33m1 -\033[m \033[0;34mVer pessoas cadastradas\033[m")
    print("\033[0;33m2 -\033[m \033[0;34mCadastrar nova Pessoa\033[m")
    print("\033[0;33m3 -\033[m \033[0;34mLimpar lista\033[m")
    print("\033[0;33m4 -\033[m \033[0;34mSair do Sistema\033[m")
    print("-" * 40)

    try:
        o = int(input("Sua opção: "))

    except(ValueError, TypeError):
        print("\033[0;31mTivemos um problema com os tipos de dados que você digitou.\033[m")
    except KeyboardInterrupt:
        print("\033[0;31mO usuário prefiriu não informar os dados.\033[m")
        break
    else:
        if o == 1 or o == 2 or o == 3 or o == 4:
            if o == 1:
                print("-" * 40)
                print("PESSOAS CADASTRADAS".center(40))
                print("-" * 40)
                try:
                    arquivos.lerarq()
                except FileNotFoundError:
                    arquivos.criararq()
                print("-" * 40)

            elif o == 2:
                print("-" * 40)
                nome = str(input("Nome: "))
                idade = arquivos.leiaint("Idade: ")
                print(f"Novo registro de {nome} adicionado.")
                try:
                    arquivos.adicioarq(f"\n{nome:<29}")
                    arquivos.adicioarq(f"{idade:>3} anos")
                except FileNotFoundError:
                    arquivos.criararq()
                print("-" * 40)
            elif o == 3:
                arquivos.criararq()
                print("O arquivo foi limpado com sucesso")
            elif o == 4:
                print("-" * 40)
                print("Saindo do sistema... Até logo!".center(40))
                print("-" * 40)
                break

        else:
            print("\033[0;31mERRO! Digite uma opção válida!\033[m")
