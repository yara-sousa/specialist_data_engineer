# 9.Crie uma classe Item com atributos nome e preço.
# Crie uma classe Carrinho que permita:

# Adicionar itens.

# Calcular o valor total da compra.

class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"


class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def calcular_total(self):
        return sum(item.preco for item in self.itens)
    def listar_itens(self):
        if not self.itens:
            print("Nenhum item no carrinho.")
        else:
            print("Itens no carrinho:")
            for item in self.itens:
                print(item)
            print(f"Total: R$ {self.calcular_total():.2f}")

