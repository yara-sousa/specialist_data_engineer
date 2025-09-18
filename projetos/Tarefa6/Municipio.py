# a) Gere um arquivo .csv com os 10 municipios com maior expectativa de vida.
# b) Gere um arquivo .csv  com os10 municipios com menor expectativa de vida.
# c) Gere um arquivo .csv com os 10 municipios com maior Indice de Mortalidade Infantil.
# D) Gere um arquivo .csv com os 10 municipios com menor Mortalidade Infantil.

class MunicipioMaior:
    def __init__(self):
        self.municipio = ""
        self.cod_municipio = 0
        self.indice_maior_expectativa_vida = 0.0
    

class MunicipioMenor:
    def __init__(self):
        self.municipio = ""
        self.cod_municipio = 0
        self.indice_menor_expectativa_vida = 0.0

class MunicipioMortalidadeMaior:
    def __init__(self):
        self.municipio = ""
        self.cod_municipio = 0
        self.indice_maior_mortalidade_infantil = 0.0

class MunicipioMortalidadeMenor:
    def __init__(self):
        self.municipio = ""
        self.cod_municipio = 0
        self.indice_menor_mortalidade_infantil = 0.0