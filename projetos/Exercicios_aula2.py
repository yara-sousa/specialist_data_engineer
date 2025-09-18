# PRATICA AULA 2 - PYTHON

import random

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
soma = 0
 
for x in range(numero1, numero2):
    print (x)
    if(x % 2 == 0):
      soma += x
 
   
 
print("A soma dos números é:", soma)


def tabuada():
  numero = int(input("Digite um número inteiro: "))
  for x in range(11):
    print(numero,"X", x, "=", numero*x )
 
 
tabuada()

def tabuada(valor):
  numero = int(input("Digite um número inteiro: "))
  resultado = 0
  for x in range(valor + 1):
    print(numero,"X", x, "=", numero*x )
    resultado += numero*x
 
  return resultado, numero
 
valor = int(input("Digite o valor da tabuada: "))
resultado = tabuada(valor)
print(resultado)

# Exercício 5

import random

def gera_numeros_inteiros(intervalo):
    for x in range(10):
        x = random.randrange(1, intervalo, passos)
        print(x)

intervalo = int(input("Digite o intervalo: "))
gera_numeros_flutuantes(intervalo, 3)

import random
 
def gera_numeros_inteiros(intervalo):
  for x in range(10):
    x = random.randint(1, intervalo)
    print(x)
intervalo = int(input("Digite o intervalo: "))
gera_numeros_inteiros(intervalo, 3) 

def gera_numeros_flutuantes(intervalo, passos):
    for x in range(10):
      x = random.randrange(1, intervalo, passos)
      print(x)
 
intervalo = int(input("Digite o intervalo: "))
gera_numeros_flutuantes(intervalo, 3)


# EXERCICIOS DE AULA 2 - PYTHON

# 1) Crie uma função que gere 10 números aleatórios e mostre-os ordenados em ordem crescente.

import random

def gera_numeros_ordenados():
    numeros = []
    for x in range(10):
        numero = random.randint(1, 100)  # Gera um número aleatório entre 1 e 100
        numeros.append(numero)
    numeros.sort()  # Ordena os números em ordem crescente
    print("Números ordenados:", numeros)

    return numeros

## Crie uma função que gere 10 números aleatórios e mostre-os ordenados em ordem crescente.
def ordenar_lista():
    lista = [random.randint(1, 100) for _ in range(10)]
    print("Original:", lista)
    lista.sort()
    print("Ordenada:", lista)
 
ordenar_lista()

## Crie uma função que gere 10 números aleatórios e mostre-os ordenados em ordem crescente.
def ordenar_lista():
    lista = [random.randint(1, 100) for _ in range(10)]
    print("Original:", lista)
    lista.sort()
    print("Ordenada:", lista)
 
ordenar_lista()
 


# 2) Crie uma função que sorteie 6 números únicos entre 1 e 60 (como uma Mega-Sena).

def sorteia_numeros_mega_sena():
    numeros = set() 
    while len(numeros) < 6:
        numero = random.randint(1, 60)
        numeros.add(numero)
    print("Números sorteados da Mega-Sena:", sorted(numeros))  # Mostra os números ordenados

    return numeros

# 3) Crie uma função que calcule a média de n números aleatórios entre 1 e 500.

def calcula_media_numeros_aleatorios(n):
    numeros = []
    for x in range(n):
        numero = random.randint(1, 500)
        numeros.append(numero)
    media = sum(numeros) / n
    print(f"Média dos números aleatórios entre 1 e 500:", media)

    return numeros
calcula_media_numeros_aleatorios(10)

# 4) Crie uma função que receba um dicionário de profissões e salários e retorne quantos salários são maiores que 10.000

dict_prof_salr = {
    "Engenheiro": 12000,
    "Médico": 15000,
    "Professor": 8000,
    "Advogado": 11000,
    "Designer": 7000
}

def conta_salarios_altos(dict_prof_salr):
    count = 0
    for salario in dict_prof_salr.values():
        if salario > 9000:
            count += 1
    print(f"Número de salários maiores que 90.000:", count)

    return count

conta_salarios_altos(dict_prof_salr)

# 5) Crie uma função que gere 20 números aleatórios e conte quantos são pares e quantos ímpares.

def conta_pares_impares():
    pares = 0
    impares = 0
    numeros_gerados = []
    for x in range(20):
        numero = random.randint(1, 100)
        numeros_gerados.append(numero)
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    print(f"Números gerados entre 1 e 100:", numeros_gerados)
    print(f"Números pares: {pares}, Números ímpares: {impares}")

    return pares, impares, numeros_gerados

conta_pares_impares()

# 6) Crie uma função que receba um dicionário representando o estoque de uma loja (produto: quantidade). Depois percorra e mostre quais produtos estão em falta (quantidade == 0).
estoque = {
    "Camiseta": 55,
    "Calça": 0,
    "Tênis": 23,
    "Bolsas": 0,
    "Meias": 18
}

def verifica_estoque(estoque):
    produtos_em_falta = []
    for produto, quantidade in estoque.items():
        if quantidade == 0:
            produtos_em_falta.append(produto)
    print("Produtos em falta no estoque:", produtos_em_falta)

    return produtos_em_falta

verifica_estoque(estoque)

#PROF

def contar_salarios(dados):
    cont = 0
    for profissao, salario in dados.items():
        if salario > 10000:
            cont += 1
    return cont
 
profissoes = {
    "Médico": 25000,
    "Professor": 5000,
    "Engenheiro": 12000,
    "Analista": 8000
}
print("Profissões com salário > 10000:", contar_salarios(profissoes))


# 7) Escreva uma função que sorteie um número entre 1 e 20. O usuário deve adivinhar até acertar.

import random

def jogo_adivinhacao():
    numero_sorteado = random.randint(1, 20)
    tentativa = None
    while tentativa != numero_sorteado:
        tentativa = int(input("Adivinhe o número entre 1 e 20: "))
        if tentativa < numero_sorteado:
            print("Muito baixo! Tente novamente.")
        elif tentativa > numero_sorteado:
            print("Muito alto! Tente novamente.")
    print("Parabéns! Você acertou o número:", numero_sorteado)

jogo_adivinhacao()

# 8) Crie uma função que receba um dicionário com nomes de alunos e notas. Depois percorra o dicionário com for e exiba cada aluno e sua nota.

alunos_notas = {
    "Yara": 85,
    "Bruno": 90,
    "Carlos": 78,
    "Lucas": 92
}


def exibe_alunos_notas(alunos_notas):
    for aluno, nota in alunos_notas.items():
        print(f"Aluno: {aluno}, Nota: {nota}")
    return alunos_notas

exibe_alunos_notas(alunos_notas)

# 9) Crie uma função que gere 15 números aleatórios entre 1 e 100 e armazene-os em uma lista. Depois, percorra a lista com for e exiba apenas os números maiores que 50.

def exibe_numeros_maiores():
    numeros  = []
    for x in range(15):
        numeros.append(random.randint(1, 100))
    for numero in numeros:
        if numero > 50:
            print("Número maior que 50:", numero)
    return numeros

exibe_numeros_maiores()

# 10) Crie uma função que receba uma lista de nomes e exiba cada nome com sua respectiva posição na lista (usando enumerate).

def exibe_nomes_com_posicao():
    nomes = ["Yara", "Lucas", "Bruno", "Carlos"]
    for indice, nome in enumerate(nomes):
        print(f"Posição: {indice}, Nome: {nome}")
        return nomes

exibe_nomes_com_posicao()


# ORIENTAÇÃO A OBJETOS - PYTHON

#Chamando uma classe 

import Carro

import Automovel


c = Carro()
c.marca =  input("Informe a Marca do veiculo:")
c.modelo =  input("Informe o Modelo do veiculo:")
c.ano =  input("Informe o ano do veiculo:")
c.chassi =  input("Informe a Chassi do veiculo:")
c.cor =  input("Informe a Cor do veiculo:")
c.imprimir()    

automovel = Automovel()
automovel.tipo = input("Informe o Tipo do automóvel:")
automovel.cor = input("Informe a Cor do automóvel:")
automovel.marca = input("Informe  a Marca do automóvel:")
automovel.modelo = input("Informe o Modelo do automóvel:")
automovel.ano_fabricacao = int(input("Informe o Ano de fabricação do automovel:"))
automovel.numero_portas = int(input("Informe o Numero de portas do automóvel:"))
automovel.chassi = input("Informe o Chassi do automóvel:")
automovel.placa = input("Informe a Placa do automóvel:")
print(vars(automovel))