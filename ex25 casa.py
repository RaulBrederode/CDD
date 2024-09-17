usuario = "Raul2004"
tentativas1 = 0
maxtentativ = 3
while tentativas1 < maxtentativ:
    usuarioo = str(input("Digite seu usuário: "))
    if usuarioo == usuario:
        print(f"Olá, {usuario}")
        break
    else:
        tentativas1 += 1
        print(f"Nome de usuário incorreto. Você tem {maxtentativ - tentativas1} tentativa(s) restante(s).")
        if tentativas1 == 2:
            print("Esta é a sua última tentativa, em caso de erro, o seu usuário será BLOQUEADO!!!")
        if tentativas1 == maxtentativ:
            print("Usuário bloqueado!")
            exit()
senha = "291304"
tentativas = 0
maxtentativas = 3
while tentativas < maxtentativas:
    senhausuario = str(input("Digite sua senha: "))
    if senhausuario == senha:
        print(f"Acesso permitido. Seja bem-vindo, {usuario}")
        break
    else:
        tentativas += 1
        print(f"Senha incorreta! Você tem {maxtentativas - tentativas} tentativa(s) restante(s).")
    if tentativas == 2:
        print("Esta é a sua última tentativa, em caso de outro erro sua senha será BLOQUEADA!!!")
    if tentativas == maxtentativas:
        print("Senha BLOQUEADA!")
        exit()
