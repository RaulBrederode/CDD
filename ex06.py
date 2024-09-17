n1 = int(input("Dê um número: "))
n2 = int(input("Dê um outro número: "))
if n1 > n2:
    print("{}, {}".format(n2, n1))
elif n1 == n2:
    print("Números iguais, por favor escreva outro número.")
    exit()
else:
    print("{}, {}".format(n1, n2))
