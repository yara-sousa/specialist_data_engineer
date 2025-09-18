# 2. Crie uma classe Carro com atributos marca e ano. Adicione um método detalhes() que mostre a marca e o ano do carro.

class Carro:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

    def detalhes(self):
        print(f"Marca: {self.marca}, Ano: {self.ano}")

