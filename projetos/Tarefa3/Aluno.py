# 5.Crie uma classe Aluno com atributos nome e notas (lista).

# Crie um método que calcule a média do aluno.

# Instancie objetos e exiba as médias.

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
       
        self.notas = notas[:6]

    def calcular_media(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

