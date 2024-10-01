notas = [0.0] * 5
tam = len(notas)
soma = 0
cont = 0
for i in range(tam):
    notas[i] = int(input("Digite a nota: "))
for x in range(tam):
    soma = soma + notas[x]
media = soma / tam
for z in range(tam):
    if notas[z] > media:
        cont = cont+1
print(f"A média da turma é {media} e {cont} alunos tiveram nota maior que a média.")
