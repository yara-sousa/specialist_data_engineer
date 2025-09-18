from Pessoa import Pessoa
from Carro import Carro
from Conta import conta
from Retangulo import Retangulo
from Area import Area 
from Aluno import Aluno
from Produto import Produto, Estoque
from Livro import Livro, Biblioteca
from Contato import Contato, Agenda
from Item import Item, Carrinho
from Forca import Forca


# Crie uma classe Pessoa com atributos nome e idade. Instancie dois objetos e exiba os dados de cada pessoa.
# Chamando Classe Pessoa 

pessoa1 = Pessoa(input("Digite seu nome: "), int(input("Digite sua idade: ")))
pessoa2 = Pessoa(input("Digite seu nome: "), int(input("Digite sua idade: ")))

pessoa1.exibir_dados()
pessoa2.exibir_dados()

# 2. Crie uma classe Carro com atributos marca e ano. Adicione um método detalhes() que mostre a marca e o ano do carro.

carro = Carro(input("Informe a Marca do veiculo:"), input("Informe o ano do veiculo:"))
carro.detalhes()

# 3.Crie uma classe Conta com atributos titular e saldo.

conta = Conta(input("Informe o nome do titular da conta: "), float(input("Informe o saldo inicial: ")))
conta.depositar(float(input("Informe o valor a ser depositado: ")))
conta.sacar(float(input("Informe o valor a ser sacado: ")))

# 4. Crie uma classe Retangulo com atributos largura e altura.

retangulo = Retangulo(float(input("Informe a largura do retângulo: ")), float(input("Informe a altura do retângulo: ")))
print(f"Área do retângulo: {retangulo.area()}")
print(f"Perímetro do retângulo: {retangulo.perimetro()}")   

# Crie métodos que retornem a área e o perímetro do retângulo.

retangulo = Area(float(input("Informe a largura do retângulo: ")), float(input("Informe a altura do retângulo: ")))
print(f"Área do retângulo: {retangulo.area()}")
print(f"Perímetro do retângulo: {retangulo.perimetro()}")


# 5.Crie uma classe Aluno com atributos nome e notas (lista).

# Crie um método que calcule a média do aluno.

# Instancie objetos e exiba as médias.

nome = input("Informe o nome do aluno: ")
notas = []
for i in range(6):
    try:
        nota = float(input(f"Informe a nota {i+1} (ou pressione Enter para parar): ") or "")
        notas.append(nota)
    except ValueError:
        break  

aluno = Aluno(nome, notas)
print(f"Média do aluno {aluno.nome}: {aluno.calcular_media():.2f}")

# 6. Crie uma classe Produto com atributos nome e preço.
# Crie uma classe Estoque que armazena produtos.

# Crie métodos para adicionar produtos e listar todos os produtos cadastrados.

estoque = Estoque()
while True:
    nome = input("Informe o nome do produto (ou pressione Enter para sair): ")
    if not nome:
        break
    try:
        preco = float(input("Informe o preço do produto: "))
        produto = Produto(nome, preco)
        estoque.adicionar_produto(produto)
    except ValueError:
        print("Preço inválido!")

estoque.listar_produtos()


# 7. Crie uma classe Livro com atributos título e autor.
# Crie uma classe Biblioteca que permita:

# Adicionar livros.

# Listar todos os livros cadastrados.

biblioteca = Biblioteca()
while True:
    titulo = input("Informe o título do livro (ou pressione Enter para sair): ")
    if not titulo:
        break
    autor = input("Informe o autor do livro: ")
    livro = Livro(titulo, autor)
    biblioteca.adicionar_livro(livro)

biblioteca.listar_livros()

# 8. Crie uma classe Contato com atributos nome e telefone.
# Crie uma classe Agenda que permita:

# Adicionar contatos.

# Pesquisar um contato pelo nome.

# Listar todos os contatos cadastrados.

agenda = Agenda()
while True:
    nome = input("Informe o nome (ou pressione Enter para sair): ")
    if not nome:
        break
    telefone = input("Informe o telefone: ")
    contato = Contato(nome, telefone)
    agenda.adicionar_contato(contato)

agenda.listar_contatos()

nome_pesquisa = input("Digite o nome para pesquisar: ")
contato_encontrado = agenda.pesquisar_contato(nome_pesquisa)
if contato_encontrado:
    print("Contato encontrado:", contato_encontrado)
else:
    print("Contato não encontrado.")



# 9.Crie uma classe Item com atributos nome e preço.
# Crie uma classe Carrinho que permita:

# Adicionar itens.

# Calcular o valor total da compra.

carrinho = Carrinho()
while True:
    nome = input("Informe o nome do item (ou pressione Enter para sair): ")
    if not nome:
        break
    try:
        preco = float(input("Informe o preço do item: "))
        item = Item(nome, preco)
        carrinho.adicionar_item(item)
    except ValueError:
        print("Preço inválido!")

carrinho.listar_itens()

# 10. Crie uma classe Forca que sorteie uma palavra de uma lista e permita que o jogador tente adivinhar, letra por letra, até acabar as tentativas ou acertar a palavra.

palavras = ["python", "desenvolvimento", "programacao", "forca", "jogo"]
jogo = Forca(palavras)
print("Bem-vindo ao jogo da Forca!")

while not jogo.jogo_terminado():
    print("\nPalavra:", jogo.mostrar_palavra())
    print("Tentativas restantes:", jogo.tentativas)
    letra = input("Digite uma letra: ")
    if jogo.adivinhar(letra):
        print("Acertou!")
    else:
        print("Errou!")

if jogo.venceu():
    print("Parabéns! Você venceu!")
else:
    print("Game over! A palavra era:", jogo.palavra)
