# 6. Crie uma classe Produto com atributos nome e preço.
# Crie uma classe Estoque que armazena produtos.

# Crie métodos para adicionar produtos e listar todos os produtos cadastrados.

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"

class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        if not self.produtos:
            print("Nenhum produto cadastrado.")
        else:
            print("Produtos cadastrados:")
            for produto in self.produtos:
                print(produto)
            
