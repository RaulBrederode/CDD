n1 = float(input("Digite a nota da sua av1: "))
while n1 < 0 or n1 > 10:
    print("Digite novamente a sua av1, (0 a 10).")
    n1 = float(input("Digite a nota da sua av1: "))
n2 = float(input("Digite a nota da sua av2: "))
while n2 < 0 or n2 > 10:
    print("Digite novamente a sua av2, (0 a 10).")
    n2 = float(input("Digite a nota da sua av2: "))
media = (n1 + n2) / 2
print(f"A sua nota da av1 é {n1} e a sua av2 é {n2}.")
print(f"Sua média é: {media}")
