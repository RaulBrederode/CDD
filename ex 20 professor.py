opcao = 1
while opcao != 2:
    x = int(input("Digite o 1° valor: "))
    y = int(input("Digite o 2° valor: "))

    while x == 0:
        print("Digite novamente o 1° valor: ")
        x = int(input("Digite o 1° valor: "))
    while y == 0:
        print("Digite novamente o 2° valor, só aceitamos valores diferentes de zero.")
        y = int(input("Digite o 2° valor: "))
    print(x/y)
    opcao = int(input("Deseja continuar:\n"
                      "[ 1 ] SIM\n"
                      "[ 2 ] NÂO\n"
                      "Sua resposta:"))
