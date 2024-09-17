opcao = 1
while opcao != 2:
    num = int(input("Digite um número: "))
    t = 0
    while t < 10:
        t += 1
        m = t * num
        print(f"{num} X {t} = {m}")
    opcao = int(input("Deseja continuar:\n"
                          "[ 1 ] SIM\n"
                          "[ 2 ] NÂO\n"
                          "Sua resposta:"))
