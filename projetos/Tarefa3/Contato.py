# 8. Crie uma classe Contato com atributos nome e telefone.
# Crie uma classe Agenda que permita:

# Adicionar contatos.

# Pesquisar um contato pelo nome.

# Listar todos os contatos cadastrados.

class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
        return f"{self.nome}: {self.telefone}"
class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)

    def pesquisar_contato(self, nome):
        for contato in self.contatos:
            if contato.nome.lower() == nome.lower():
                return contato
        return None

    def listar_contatos(self):
        if not self.contatos:
            print("Nenhum contato cadastrado.")
        else:
            print("Contatos cadastrados:")
            for contato in self.contatos:
                print(contato)

