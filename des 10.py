hora1 = int(input("Digite a hora da primeira entrada: "))
min1 = int(input("Digite os minutos da primeira entrada: "))
hora2 = int(input("Digite a hora da segunda entrada: "))
min2 = int(input("Digite os minutos da segunda entrada: "))


if hora1 > 12:
    hora1 = hora1 - 12
if hora2 > 12:
    hora2 = hora2 - 12

somah = int((hora1 + hora2))
if somah > 12:
    somah = somah - 12
somam = int((min1 + min2))

if somam >= 60:
    somam = somam - 60
    somah = somah - 1
if somah > 12:
    somah-= 12
print(f"{somah}: {somam: 02d}")
