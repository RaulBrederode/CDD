opcao = 1
while opcao == 1:
    a = int(input("Digite um número: "))
    if a % 2 == 0 and a > 0:
        print(f"O número {a} é par e positivo")
    if a % 2 == 0 and a < 0:
        print(f"O número {a} é par e negativo")
    if a % 2 != 0 and a > 0:
        print(f"O número {a} é ímpar e positivo")
    if a % 2 != 0 and a < 0:
        print(f"O número {a} é ímpar e negativo.")
    opcao = int(input("Deseja continuar?\n"
                      "[ 1 ] SIM\n"
                      "[ 2 ] NÃO\n"
                      "Sua resposta: "))
