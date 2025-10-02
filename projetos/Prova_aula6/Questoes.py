import pandas as pd
from Populacao import Populacao
import json
import os
import re

nome_arquivo = "projetos/Prova_aula6/População_SP.xlsx"
lista = le_arquivo(nome_arquivo)

def le_arquivo(nome_diretorio):
    lista = []
    arquivo = open(nome_diretorio, "r", encoding="utf-8")
    tamanho = arquivo.readlines()
    cont = 0

    while(cont < len(tamanho)):
        linha = tamanho[cont]
        vetor = re.split(r';|\n', linha)
        c = Populacao(vetor[0], int(vetor[1]), int(vetor[2]))
        lista.append(c)
        cont += 1
       
    arquivo.close()
    return lista
def gerar_excel_json():
    dados = [vars(p) for p in lista]
    df = pd.DataFrame(dados)
    df.to_excel("projetos/Prova_aula6/populacao.xlsx", index=False)
    df.to_json("projetos/Prova_aula6/populacao.json", orient='records', force_ascii=False)
    print("Fim do Processamento ....")
gerar_excel_json()
def faixa_etaria_mais_populosa(lista):
    if not lista:
        return None

    faixa_mais_populosa = max(lista, key=lambda p: p.total)
    return faixa_mais_populosa
faixa_mais_populosa = faixa_etaria_mais_populosa(lista)
if faixa_mais_populosa:
    print(f"A faixa etária com mais pessoas é: {faixa_mais_populosa.faixa_etaria} com um total de {faixa_mais_populosa.total} pessoas.")
else:
    print("A lista está vazia.")    
