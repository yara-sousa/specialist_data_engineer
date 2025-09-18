from MunicipioIDH import MunicipioIDH
 
def leArquivo(nomeDiretorio):
    arquivo = open(nomeDiretorio, "r", encoding="utf-8")
    tamanho = arquivo.readlines()
    cont = 0
    lista_municipios = []
   
    while(cont < len(tamanho)):
        if(cont == 0 ):
            cont += 1
            continue
       
        linha = tamanho[cont]
        dados = linha.split(";")
        municipio = MunicipioIDH()
        municipio.cod_municipio = int(dados[0])
        municipio.municipio = dados[1]
        municipio.indice_expectativa_vida = float(dados[2].replace(",", "."))
        municipio.indice_mortalidade_infantil = float(dados[3].replace(",", "."))
        cont += 1
        lista_municipios.append(municipio)
       
    arquivo.close()
    return lista_municipios
   
   
arquivo_entrada = "IDH2010.csv"
 
lista_processada = leArquivo(arquivo_entrada)
 
for dados in lista_processada:
    print("Nome Municipio ...: " + dados.municipio + " Expectativa de Vida ..: " + str(dados.indice_expectativa_vida) + " Mortalidade Infantil ..: " + str(dados.indice_mortalidade_infantil))



def leArquivo(nomeDiretorio):
    arquivo = open(nomeDiretorio, "r", encoding="utf-8")
    tamanho = arquivo.readlines()
    cont = 0
    lista_municipios = []
   
    while(cont < len(tamanho)):
        if(cont == 0 ):
            cont += 1
            continue
       
        linha = tamanho[cont]
        dados = linha.split(";")
        municipio = MunicipioIDH()
        municipio.cod_municipio = int(dados[0])
        municipio.municipio = dados[1]
        municipio.indice_expectativa_vida = float(dados[2].replace(",", "."))
        municipio.indice_mortalidade_infantil = float(dados[3].replace(",", "."))
        cont += 1
        lista_municipios.append(municipio)
       
    arquivo.close()
    return lista_municipios
   
   
arquivo_entrada = "IDH2010.csv"
 
lista_processada = leArquivo(arquivo_entrada)
arquivo_saida_vida = "MunicipiosExpectativa.csv"
lista_processada.sort(key=lambda idh: idh.indice_expectativa_vida)
 
arquivo_vida = open(arquivo_saida_vida, "w+", encoding="utf-8")  
for dados in lista_processada:
    arquivo_vida.write(dados.municipio + ";"  + str(dados.indice_expectativa_vida) + "\n")
 
arquivo_vida.close()  