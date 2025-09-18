# Crie uma classe Pessoa com atributos nome e idade. Instancie dois objetos e exiba os dados de cada pessoa.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")
    
pessoa1 = Pessoa(input("Digite seu nome: "), int(input("Digite sua idade: ")))
pessoa2 = Pessoa(input("Digite seu nome: "), int(input("Digite sua idade: ")))

pessoa1.exibir_dados()
pessoa2.exibir_dados()
