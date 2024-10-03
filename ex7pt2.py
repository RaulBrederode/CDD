usuarray = ["1"]*5
senhaaarray = ["1"]*5
tam = len(usuarray)
for x in range(tam):
    usuarray[x] = str(input("Digite seu usuário: "))
    senhaaarray[x] = str(input("Digite sua senha: "))
for z in range(tam):
    print(f"O usuário {usuarray[z]} tem a senha {senhaaarray[z]} e sua posição é {z}")
