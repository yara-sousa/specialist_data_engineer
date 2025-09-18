# Com base no diagrama abaixo crie a classe mãe com suas respectivas classes filha com no mínimo 2 atributos para cada classe criada. Onde a classe Animal herdara as classes gato, coelho e cachorro.

class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_som(self):
        pass

class Gato(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def fazer_som(self):
        print("Miau")

class Coelho(Animal):
    def __init__(self, nome, idade, cor):
        super().__init__(nome, idade)
        self.cor = cor

    def fazer_som(self):
        print("Som de coelho")

class Cachorro(Animal):
    def __init__(self, nome, idade, porte):
        super().__init__(nome, idade)
        self.porte = porte

    def fazer_som(self):
        print("Au Au")
