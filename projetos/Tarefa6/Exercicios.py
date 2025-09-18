from Municipio import MunicipioMaior, MunicipioMenor, MunicipioMortalidadeMaior, MunicipioMortalidadeMenor

# a) Gere um arquivo .csv com os 10 municipios com maior expectativa de vida.

def gerar_csv_maior_expectativa_vida(nomeDiretorio, nomeArquivoSaida):
    arquivo = open(nomeDiretorio, "r", encoding="utf-8")
    linhas = arquivo.readlines()
    arquivo.close()

    lista_municipios = []
    for linha in linhas[1:]:  # pula o cabeçalho
        dados = linha.strip().split(";")
        municipio = MunicipioMaior()
        municipio.cod_municipio = int(dados[0])
        municipio.municipio = dados[1]
        municipio.indice_expectativa_vida = float(dados[2].replace(",", "."))
        lista_municipios.append(municipio)

    lista_municipios.sort(key=lambda x: x.indice_expectativa_vida, reverse=True)
    top_10 = lista_municipios[:10]

    arquivo_saida = open(nomeArquivoSaida, "w", encoding="utf-8")
    arquivo_saida.write("cod_municipio;municipio;indice_expectativa_vida\n")
    for municipio in top_10:
        arquivo_saida.write(f"{municipio.cod_municipio};{municipio.municipio};{municipio.indice_expectativa_vida}\n")
    arquivo_saida.close()

gerar_csv_maior_expectativa_vida("IDH2010.csv", "MaiorExpectativa.csv")

# b) Gere um arquivo .csv  com os10 municipios com menor expectativa de vida.

def gerar_csv_menor_expectativa_vida(nomeDiretorio, nomeArquivoSaida):
    arquivo = open(nomeDiretorio, "r", encoding="utf-8")
    linhas = arquivo.readlines()
    arquivo.close()

    lista_municipios = []
    for linha in linhas[1:]: 
        dados = linha.strip().split(";")
        municipio = MunicipioMenor()
        municipio.cod_municipio = int(dados[0])
        municipio.municipio = dados[1]
        municipio.indice_expectativa_vida = float(dados[2].replace(",", "."))
        lista_municipios.append(municipio)

    lista_municipios.sort(key=lambda x: x.indice_expectativa_vida)
    top_10 = lista_municipios[:10]

    arquivo_saida = open(nomeArquivoSaida, "w", encoding="utf-8")
    arquivo_saida.write("cod_municipio;municipio;indice_expectativa_vida\n")
    for municipio in top_10:
        arquivo_saida.write(f"{municipio.cod_municipio};{municipio.municipio};{municipio.indice_expectativa_vida}\n")
    arquivo_saida.close()

gerar_csv_menor_expectativa_vida("IDH2010.csv", "MenorExpectativa.csv")

# c) Gere um arquivo .csv com os 10 municipios com maior Indice de Mortalidade Infantil.

def gerar_csv_maior_mortalidade_infantil(nomeDiretorio, nomeArquivoSaida):
    arquivo = open(nomeDiretorio, "r", encoding="utf-8")
    linhas = arquivo.readlines()
    arquivo.close()

    lista_municipios = []
    for linha in linhas[1:]: 
        dados = linha.strip().split(";")
        municipio = MunicipioMortalidadeMaior()
        municipio.cod_municipio = int(dados[0])
        municipio.municipio = dados[1]
        municipio.indice_mortalidade_infantil = float(dados[3].replace(",", "."))
        lista_municipios.append(municipio)

    lista_municipios.sort(key=lambda x: x.indice_mortalidade_infantil, reverse=True)
    top_10 = lista_municipios[:10]

    arquivo_saida = open(nomeArquivoSaida, "w", encoding="utf-8")
    arquivo_saida.write("cod_municipio;municipio;indice_mortalidade_infantil\n")
    for municipio in top_10:
        arquivo_saida.write(f"{municipio.cod_municipio};{municipio.municipio};{municipio.indice_mortalidade_infantil}\n")
    arquivo_saida.close()

gerar_csv_maior_mortalidade_infantil("IDH2010.csv", "MaiorMortalidadeInfantil.csv")

# D) Gere um arquivo .csv com os 10 municipios com menor Mortalidade Infantil.

def gerar_csv_menor_mortalidade_infantil(nomeDiretorio, nomeArquivoSaida):
    arquivo = open(nomeDiretorio, "r", encoding="utf-8")
    linhas = arquivo.readlines()
    arquivo.close()

    lista_municipios = []
    for linha in linhas[1:]: 
        dados = linha.strip().split(";")
        municipio = MunicipioMortalidadeMenor()
        municipio.cod_municipio = int(dados[0])
        municipio.municipio = dados[1]
        municipio.indice_mortalidade_infantil = float(dados[3].replace(",", "."))
        lista_municipios.append(municipio)

    lista_municipios.sort(key=lambda x: x.indice_mortalidade_infantil)
    top_10 = lista_municipios[:10]

    arquivo_saida = open(nomeArquivoSaida, "w", encoding="utf-8")
    arquivo_saida.write("cod_municipio;municipio;indice_mortalidade_infantil\n")
    for municipio in top_10:
        arquivo_saida.write(f"{municipio.cod_municipio};{municipio.municipio};{municipio.indice_mortalidade_infantil}\n")
    arquivo_saida.close()

gerar_csv_menor_mortalidade_infantil("IDH2010.csv", "MenorMortalidadeInfantil.csv")
