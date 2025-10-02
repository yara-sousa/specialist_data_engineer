import Piloto from Piloto
import pandas as pd

 
 
def leArquivo(nomeArquivo):
    campeoes = []
    arquivo = open(nomeArquivo, "r", encoding="UTF-8")
    tamanho = arquivo.readlines()
    cont = 0
    while(len(tamanho) > cont):
        p = Piloto()
        linha = tamanho[cont]
        dados = linha.split(";")
        p.anoTitulo = int(dados[0])
        p.nacionalidade = dados[1]
        p.nomePiloto = dados[2].replace("1","").strip()
        p.equipe = dados[3].strip()
        cont += 1  
        campeoes.append(p)
    arquivo.close()
    return campeoes
 
nome_arquivo = "projetos\formula1 3.csv"
lista = leArquivo(nome_arquivo)
 
dados = [vars(p) for p in lista]
 
df = pd.DataFrame(dados)
df.to_excel("projetos\formula1 3.csv.xlsx")

 
class Piloto:
    def __init__(self):
        self.anoTitulo = int(0)
        self.nacionalidade = ""
        self.nomePiloto = ""
        self.equipe = ""
 
def leArquivo(nomeArquivo):
    campeoes = []
    arquivo = open(nomeArquivo, "r", encoding="UTF-8")
    tamanho = arquivo.readlines()
    cont = 0
    while(len(tamanho) > cont):
        p = Piloto()
        linha = tamanho[cont]
        dados = linha.split(";")
        p.anoTitulo = int(dados[0])
        p.nacionalidade = dados[1]
        p.nomePiloto = dados[2].replace("1","").strip()
        p.equipe = dados[3].strip()
        cont += 1  
        campeoes.append(p)
    arquivo.close()
    return campeoes
 
nome_arquivo = "formula1.txt"
lista = leArquivo(nome_arquivo)
 
dados = [vars(p) for p in lista]
 
df = pd.DataFrame(dados)
df.to_excel("Formula1.xlsx")
 