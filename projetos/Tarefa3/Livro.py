# 7. Crie uma classe Livro com atributos título e autor.
# Crie uma classe Biblioteca que permita:

# Adicionar livros.

# Listar todos os livros cadastrados.

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"'{self.titulo}' de {self.autor}"

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro cadastrado.")
        else:
            print("Livros cadastrados:")
            for livro in self.livros:
                print(livro)