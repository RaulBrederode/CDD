def adicionar_nome():
    with open("arquivo.txt", "a") as arquivo:
        nome = input("Digite um nome: ")
        arquivo.write(f"{nome}\n")
        print(f"{nome} foi adicionado com sucesso.")

def mostrar_conteudo():
    with open("arquivo.txt", "r") as arquivo:
        print(arquivo.read())

def pesquisar_nome():
    nome_pesquisa = input("Digite o nome que deseja pesquisar: ")
    with open("arquivo.txt", "r") as arquivo:
        conteudo = arquivo.readlines()
        encontrado = False
        for linha in conteudo:
            if nome_pesquisa in linha:
                print(f"Nome encontrado: {linha.strip()}")
                encontrado = True
                break
        if not encontrado:
            print("Nome não encontrado.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar nome")
        print("2. Mostrar conteúdo do arquivo")
        print("3. Pesquisar nome no arquivo")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_nome()
        elif opcao == '2':
            mostrar_conteudo()
        elif opcao == '3':
            pesquisar_nome()
        elif opcao == '4':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
