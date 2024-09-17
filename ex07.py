n1 = float(input("Qual a primeira nota? "))
n2 = float(input("Qual a segunda nota? "))
n3 = float(input("Qual a terceira nota? "))
nt = (n1 + n2 + n3) / 3
if nt >= 7:
    print("Você foi aprovado!")
elif nt >= 4:
    print("Você está em recuperação!")
else:
    print("Você foi reprovado!")
