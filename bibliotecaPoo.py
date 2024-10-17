class Pessoa:
    def __init__(self, nome, peso, idade):  # método construtor
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.estado = "parado"  # Estado inicial: parado

    def mudar_estado(self, novo_estado):
        if self.estado == novo_estado:
            print(f"{self.nome} já está {novo_estado}.")
        elif self.estado == "dormindo" and novo_estado != "parado":
            print(f"{self.nome} está dormindo e precisa acordar para {novo_estado}.")
        elif self.estado == "comendo" and novo_estado == "andando":
            print(f"{self.nome} está comendo e precisa parar de de comer para andar")
        else:
            self.estado = novo_estado
            print(f"{self.nome} agora está {novo_estado}.")

    def andar(self):
        if self.estado == "dormindo":
            print(f"{self.nome} precisa acordar antes de andar.")
        else:
            self.mudar_estado("andando")

    def comer(self):
        if self.estado == "dormindo":
            print(f"{self.nome} precisa acordar antes de comer.")
        else:
            self.mudar_estado("comendo")

    def dormir(self):
        if self.estado == "andando":
            print(f"{self.nome} precisa parar de {self.estado} antes de dormir.")
        if self.estado == "comendo":
            print(f"{self.nome} precisa parar de comer antes de dormir.")
        else:
            self.mudar_estado("dormindo")

    def parar_de_andar(self):
        if self.estado == "andando":
            self.mudar_estado("parado")
        else:
            print(f"{self.nome} não está andando.")

    def parar_de_comer(self):
        if self.estado == "comendo":
            self.mudar_estado("parado")
        else:
            print(f"{self.nome} não está comendo.")

    def parar_de_dormir(self):
        if self.estado == "dormindo":
            self.mudar_estado("parado")
        else:
            print(f"{self.nome} não está dormindo.")


class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor


    def Comer(self):
        print(f"O {self.nome} está comendo.")


class Gato(Animal):  # Herança da classe Animal
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def miar(self):
        print(f"O {self.nome} foi miar...")
        print(f"O {self.nome} fez MIAU MIAU...")


class Cachorro(Animal):
    def __init__(self,nome, cor):
        super().__init__(nome, cor)

    def latir(self):
        print(f"O {self.nome} foi latir ...")
        print(f"O {self.nome} fez AU AU AU...")


class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def guinchar(self):
        print(f"O {self.nome} foi guinchar...")
        print(f"O {self.nome} fez iii iii...")


class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def mugir(self):
        print(f"O {self.nome} foi mugir...")
        print(f"O {self.nome} fez MUUUUU...")
