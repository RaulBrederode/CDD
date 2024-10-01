a = [0] * 5
tam = len(a)
for x in range(tam):
    a[x] = int(input("Digite um número: "))
for i in range(tam-1, -1, -1):
    print(a[i])
    