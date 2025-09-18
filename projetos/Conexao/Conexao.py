import mysql.connector
from Professor import Professor
 
con = mysql.connector.connect(host='localhost', database='puc', user='root', password='')
if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão ", db_info)
    cursor = con.cursor()
 
 
def fechaConexao():
    if con.is_connected():
        cursor.close()
        con.close()
        print("Conexão ao MySQL foi encerrada")
       

       
 
def incluirProfessor(professor):
    url = "INSERT INTO professor (id, nome_professor, curso, turma) VALUES ( " + str(professor.id) + ",' " + professor.nome + "', '" + professor.curso + "', '" + professor.turma + "'" + " )"
    cursor.execute(url)
    con.commit()
   
def alterarProfessor(professor):
    url = "UPDATE professor set id = " + str(professor.id) + "," + "nome_professor = " + "'" + professor.nome + "' , " + "curso = ' " + professor.curso + "' , " + " turma = " + "' " + professor.turma + "'" + " Where id = " + str(professor.id)
    cursor.execute(url)
    con.commit()
   
def deleteProfessor(professor):
    url = "delete from professor Where id = " + str(professor.id)
    cursor.execute(url)
    con.commit()
   
def pesquisarTodos():
    url = "select * from professor"
    cursor.execute(url)
    result = cursor.fetchall()
    listaProfessor = []
   
    for linha in result:
        print(linha)
        professor = Professor()
        professor.id = int(linha[0])
        professor.nome = linha[1]
        professor.curso = linha[2]
        professor.turma = linha[3]
     
        listaProfessor.append(professor)
       
    for p in listaProfessor:
        print(p.nome)
        print(p.turma)
       
 
professor = Professor()
professor.nome = input("Digite seu Nome: ")
professor.curso = input("Digite seu Curso: ")
professor.turma = input("Digite sua Turma: ")    
incluirProfessor(professor)
fechaConexao()


 
class MunicipioIDH:
    def __init__(self):
        self.ano = 0
        self.estado = ""
        self.municipio = ""
        self.cod_municipio = 0
        self.cod_UF = ""
        self.indice_mortalidade_infantil = 0.0
        self.indice_expectativa_vida = 0.0
       
class MunicipioDAO:
   
    def __init__(self):
        self.con = mysql.connector.connect(host='localhost', database='puc', user='root', password='')
        if self.con.is_connected():
            db_info = self.con.get_server_info()
            print("Conectado ao servidor MySQL versão ", db_info)
            self.cursor = self.con.cursor()
 
    def fechaConexao(self):
        if self.con.is_connected():
            self.cursor.close()
            self.con.close()
            print("Conexão ao MySQL foi encerrada")
           
    def incluir(self, Municipio):
        if self.con.is_connected():
            url = "INSERT INTO idh_mg (cod_municipio, municipio, indice_mortalidade_infantil, indice_expectativa_vida) VALUES ( " + str(Municipio.cod_municipio) + ", '" + Municipio.municipio + "'," + str(Municipio.indice_mortalidade_infantil) + ", " + str(Municipio.indice_expectativa_vida)  + " )"
            print(url)
            self.cursor.execute(url)
            self.con.commit()    
        else:
            print("Conexão Fechada ...")    
           
    def leArquivo(self, nomeDiretorio):
        arquivo = open(nomeDiretorio, "r", encoding="utf-8")
        tamanho = arquivo.readlines()
        cont = 0
        lista_municipios = []
       
        while(cont < len(tamanho)):
            if(cont == 0 ):
                cont += 1
                continue
           
            linha = tamanho[cont]
            vetor = linha.split(";")
            municipio = MunicipioIDH()
            municipio.cod_municipio = int(vetor[0])
            municipio.municipio = vetor[1]
            municipio.indice_expectativa_vida = float(vetor[2].replace(",", "."))
            municipio.indice_mortalidade_infantil = float(vetor[3].replace(",", "."))
            cont += 1
            lista_municipios.append(municipio)
            self.incluir(municipio)
           
        arquivo.close()
        return lista_municipios
   
dao = MunicipioDAO()
dao.leArquivo("IDH2010.csv")