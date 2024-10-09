class Pessoa:
    def __init__(self, n, p, i):
        self.nome = n
        self.peso = p
        self.idade = i
    def andar(self):
        print(f"{self.nome} está andando.")


    def comendo(self):
        resposta = str(input(f"{self.nome} está comendo?\n"
                             f"[ 1 ] True\n"
                             f"[ 2 ] False\n"
                             f"Sua resposta: "))
        if resposta == "1" is True:
            print("Está comendo.")
            if resposta == True:
                print(f"{self.nome} já está comendo, não pode comer mais.")
        elif resposta != "1" is False:
            print("Não está comendo.")


    def dormir(self):
        print(f"{self.nome} foi dormir.")

