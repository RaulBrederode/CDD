a = [0] * 10
m = [0] * 10
tam = len(a)
for i in range(tam):
    a[i] = int(input("Digite os números: "))
mult = int(input("Digite o multiplicador: "))

for z in range(tam):
    m[z] = a[z] * mult
    print(m)