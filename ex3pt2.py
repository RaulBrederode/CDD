nomes = [""]*5
tam = len(nomes)
for i in range(0, tam, 1):
    nomes[i] = input("Digite um nome: ")
for x in range(tam):
    print(f"Posição: {x} Nome: {nomes[x]}")

