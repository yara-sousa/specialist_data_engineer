class Carro:
   
    def __init__(self):
        self.ano = 0
        self.modelo = ""
        self.chassi = ""
        self.marca = ""
        self.cor = ""
 
    def imprimir(self):
        print("Marca ....: ", self.marca)
        print("Modelo ...: ", self.modelo)
        print("Ano ......: ", self.ano)
        print("Cor ......: ", self.cor)
        print("Chassi ...: ", self.chassi)
 
 
c = Carro()
c.marca =  input("Informe a Marca do veiculo:")
c.modelo =  input("Informe o Modelo do veiculo:")
c.ano =  input("Informe o ano do veiculo:")
c.chassi =  input("Informe a Chassi do veiculo:")
c.cor =  input("Informe a Cor do veiculo:")
c.imprimir()

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


 