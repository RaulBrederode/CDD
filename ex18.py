n = 1
soma = 0
while n<=10:
    print(f"Estamos no passo {n} e a soma é {soma}")
    num = int(input("Digite um número: "))
    soma = soma + num
    n = n + 1  # mesma coisa que: n+=1
media = soma/10
print(int(media))
