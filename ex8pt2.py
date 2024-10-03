numarray = [0]*10
tam = len(numarray)
cont = 0
for x in range(tam):
    numarray[x] = int(input(f"{x} Digite um número: "))
usuario = int(input("Digite um número para pesquisar: "))
#for z in range(tam):
    #if usuario == numarray[z]:
        #cont+=1
print(numarray.count(usuario))
