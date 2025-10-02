import mysql.connector
import pandas as pd
from Formula1 import Formula1
 
 
 
 
con = mysql.connector.connect(host='localhost', database='puc', user='root', password='')
if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão ", db_info)
    cursor = con.cursor()
 
 
def fecha_conexao():
    if con.is_connected():
        cursor.close()
        con.close()
        print("Conexão ao MySQL foi encerrada")
 
       
def incluir(formula1):
    url = "INSERT INTO formula1 (ano, nome, equipe, nacionalidade) VALUES ( " + str(formula1.ano) + ",' " + formula1.nome + "', '" + formula1.equipe + "', '" + formula1.nacionalidade + "'" + " )"
    print(url)
    cursor.execute(url)
    con.commit()
   
def le_arquivo(nomeDiretorio):
    lista = []
    arquivo = open(nomeDiretorio, "r", encoding="utf-8")
    tamanho = arquivo.readlines()
    cont = 0
 
    while(cont < len(tamanho)):
        linha = tamanho[cont]
        vetor = linha.split(";")
        c = Formula1()
        c.ano = int(vetor[0])
        c.nacionalidade = vetor[1]      
        c.nome = vetor[2].replace("1", "").strip()
        c.equipe = vetor[3]
        lista.append(c)
        cont += 1
       
    arquivo.close()
    return lista
 
def gerar_excel_json():
    sql_query = pd.read_sql_query ('''
    SELECT f.ano as Ano, f.nome as Nome, f.nacionalidade as Nacionalidade, f.equipe as Equipe FROM Formula1 f order by f.nome
                                   ;''', con)
 
    sql_query.to_excel('formula1.xlsx', index=False)
    sql_query.to_json('formula1.json', orient='records')
 
    print("Fim do Processamento ....")
 
 
lista = le_arquivo("formula1.csv")
 
for formula1 in lista:
    incluir(formula1)
     
 
fecha_conexao()