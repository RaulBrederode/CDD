num = [0]*10
maior = 1000000000000000000000000
menor = -10000000000
for x in range(10):
    num[x] = int(input("Digite os números: "))
for i in range(10):
    if num[i] % 2 == 0:
        print(f"Este número é par: {num[i]}")
for y in range(10):
    if num[y] > maior:
        maior = num[y]
    if num [y] < menor
        print(maior)