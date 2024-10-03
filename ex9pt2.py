nomes = [""]*5
tam = len(nomes)
for x in range(5):
    nomes[x] = str(input("Digite os nomes: "))
print(nomes)
nomes.reverse()
print(nomes)
#for z in range(4, -1, -1):
    #print(nomes[z], end=" ")