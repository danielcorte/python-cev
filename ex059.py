# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
n1 = float(input("Primeiro valor: "))
n2 = float(input("Segundo valor: "))
opc = 0
while opc != 5:
    print("[1] somar\n"
          "[2] multiplicar\n"
          "[3] maior\n"
          "[4] novos números\n"
          "[5] sair do programa")
    opc = int(input(">>>> Qual é a sua opção?? "))
    if opc == 1:
        soma = n1 + n2
        print(f"A soma entre {n1} e {n2} é {soma}")
    elif opc == 2:
        produto = n1 * n2
        print(f"O resultado de {n1} x {n2} é {produto}")
    elif opc == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f"Entre {n1} e {n2} o maior valor é {maior}")
    elif opc == 4:
        print("Informe os números novamente:")
        n1 = float(input("Primeiro valor: "))
        n2 = float(input("Segundo valor: "))
    elif opc == 5:
        "Finalizando..."
    else:
        print("Opção inválida! Tente novamente.")
    print("=-=" * 10)
print("Fim do programa. Volte sempre!!")
