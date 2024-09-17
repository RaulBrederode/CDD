num = int(input("Digite um número: "))
for i in range(1, num+1, 2):
    if i % 2 != 0:
        print(f"{i}")
        