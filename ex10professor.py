num = [0]*10
maior = 0
menor = num[0]
for x in num:
    if x%2==0:
        print(x,end=" ")

for y in num:
    if y > maior:
        maior=y
    if y < menor:
        menor=y
print()
print(maior)
print(menor)
max(num)
min(num)