soma = 0
aluno = int(input("Digite o número de alunos: "))
for x in range(1, aluno+1, 1):
    num = float(input(f"Digite a nota do aluno {x}: "))
    soma = soma + num
mediaa = soma / aluno
print(mediaa)
