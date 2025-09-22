#Exercícios de aula 2 - Python

# 1)Crie uma classe automóvel com os seguintes atributos:
# a)Tipo do automóvel; Cor; Marca; Modelo; Ano de fabricação; Numero de
# portas; Chassi; Placa.
# b)Crie cinco instâncias diferentes da classe criada, digitada pela usuário.

class Automovel:

    def __init__(self):
        self.tipo  = ""
        self.cor = ""
        self.marca = ""
        self.modelo = ""
        self.ano_fabricacao = 0
        self.numero_portas = 0  
        self.chassi = ""
        self.placa = ""

# 2) Crie os seguintes métodos para a classe criada.
# a)Liga, Desligar, frear; acelerar; travar portas
# b)Insira uma mensagem dentro de cada metodo quando o mesmo for
# invocado.
# c)Crie um método Imprimir recebendo por parametro Automóvel e
# imprimindo seus atributos

    def ligar(self):
        print("O automóvel está ligado.")

    def desligar(self):
        print("O automóvel está desligado.")

    def frear(self):
        print("O automóvel está freando.")

    def acelerar(self):
        print("O automóvel está acelerando.")

    def travar_portas(self):
        print("As portas do automóvel estão travadas.")

    def imprimir(self, automovel):
        print("Tipo:", automovel.tipo)
        print("Cor:", automovel.cor)
        print("Marca:", automovel.marca)
        print("Modelo:", automovel.modelo)
        print("Ano de Fabricação:", automovel.ano_fabricacao)
        print("Número de Portas:", automovel.numero_portas)
        print("Chassi:", automovel.chassi)
        print("Placa:", automovel.placa)
# 3) Crie uma função que receba um dicionário com nomes de alunos e suas respectivas notas. A função deve percorrer o dicionário com for e exibir cada aluno com sua nota.

alunos_notas = {
    "Yara": 9.5,
    "Bruno": 8.0,
    "Carlos": 7.5,
    "Lucas": 9.0
}

def exibe_alunos_notas(alunos_notas):
    for aluno, nota in alunos_notas.items():
        print(f"Aluno: {aluno}, Nota: {nota}")
    return alunos_notas

exibe_alunos_notas(alunos_notas)
# 4) Crie uma função que gere 15 números aleatórios entre 1 e 100 e armazene-os em uma lista. Depois, percorra a lista com for e exiba apenas os números maiores que 50.
import random