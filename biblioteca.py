def par(n):
    if n % 2 == 0:
        print("Número é par.")
def impar(n):
    if n % 2 != 0:
        print("Número ímpar.")
usuarios = []
senhas = []
def cadastro():
    usuarios = []
    senhas = []
    nome = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    usuarios.append(nome)
    senhas.append(senha)
    print("Usuário cadastrado com sucesso!")
def mostrar():
    for i in range(len(usuarios)):
        print(f"Usuário: {usuarios[i]}")
        print(f"Senha: {senhas[i]}")
def login():
    nomelogin = input("Digite o nome de usuário: ")
    senhalogin = input("Digite a senha: ")
    if nomelogin in usuarios:
        indice = usuarios.index(nomelogin)
        if senhalogin == senhas[indice]:
            print("Login efetuado com sucesso!")
        else:
            print("Senha incorreta. Tente novamente.")
    else:
        print("Usuário não encontrado. Por favor, verifique o nome de usuário.")

def imprimenome(nome):
    print(f"Nome: {nome}")

def numerospiramide(num):
    for x in range(1, num + 1):
        for z in range(0, x):
            print(x, end=" ")
        print()

def piramide(num):
    for x in range(1, num + 1):
        for z in range(1, 1 + x):
            print(z, end=" ")
        print()
def contarvogais(texto):
    # procedimento
    conte = 0
    t = len(texto)
    for x in range(t):
        if texto[x] in "aeiouAEIOU":
            conte+=1
    print(f"Encontramos {conte} vogais.")

def contarvogais1(texto):
    # função
    conte = 0
    t = len(texto)
    for x in range(t):
        if texto[x] in "aeiouAEIOU":
            conte+=1
    return(conte)
def somar(*numeros):
    soma = sum(numeros)
    print(soma)

def contarletras(texto):
    tam = len(texto) - texto.count(" ")
    print(tam)
    textocontrario = ''.join(reversed(texto))
    print(textocontrario)

def tirarnúmerosrepetidos(lista):
    # ex: a = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4]
    #tirarnúmeros repetidos(a) == [1,2,3,4]
    novalista = []
    for x in lista:
        if x not in novalista:
            novalista.append(x)
    print(novalista)
def numprimos(n):
    if (n == 1):
        return n, "Não é Primo"
    elif (n == 2):
        return n, "É Primo"
    else:
        for x in range(2,n):
            if(n%x ==0):
                return n, "Não é Primo"
            return n, "É Primo"