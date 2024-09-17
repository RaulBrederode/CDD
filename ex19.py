n = 0
nota = 0
aluno = int(input("Digite o número de alunos: "))
while n < aluno:
    num = int(input("Digite um número: "))
    nota = nota + num
    n = n + 1
media = nota / aluno
print(int(media))