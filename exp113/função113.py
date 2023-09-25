def leiafloat():
    while True:
        try:
            entradaint = int(input("Digite um número inteiro: ").replace(",", "."))
        except(ValueError, TypeError):
            print("\033[0;31mTivemos um problema com os tipos de dados que você digitou.\033[m")
        except KeyboardInterrupt:
            print("\033[0;31mO usuário preferiu não informar os dados.\033[m")
        else:
            break
    while True:
        try:
            entradareal = float(input("Digite um número real: ").replace(",", "."))
        except(ValueError, TypeError):
            print("\033[0;31mTivemos um problema com os tipos de dados que você digitou.\033[m")
        except KeyboardInterrupt:
            print("\033[0;31mO usuário preferiu não informar os dados.\033[m")
        else:
            print(f"\033[0;34mO valor inteiro digitado foi {entradaint} e o real foi {entradareal}\033[m")
            break
    print("Programa finalizado. Obrigado volte sempre!")
