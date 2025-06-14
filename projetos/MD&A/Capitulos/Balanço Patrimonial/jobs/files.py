import pandas as pd 
import os
from datetime import datetime
from decimal import Decimal


# Variaveis globais
BUCKET_OUTPUT = "yara-coe-code"
BUCKET_PATH = "MD&A/Capitulos/Balanço Patrimonial/input"
PATH_NAME = "tb_ri0_mdea_rules_bal_patr.csv"
PATH = f"C:\\Users\\Ysnun\\OneDrive\\Documentos\\Yara\\CoeCode\\MD&A\\Capitulos\\Balanço Patrimonial\\input\\{PATH_NAME}"
SERVICE = "job de regras do Capítulo Balanço Patrimonial"

def normalize_balanco_patrimonial(df):
    """Função que realiza a normalização do arquivo de Balanço Patrimonial."""
    try:
        df = pd.read_csv(
            PATH, 
            sep=",", 
            encoding="utf-8", 
            decimal=".",
            index_col=False,
        )
        colunas = ['nom_atbt', 'nom_arq_orig', 'nom_top', 'nom_agrp', 'nom_cap']
        df[colunas] = df[colunas].astype(str).replace("'", "", regex=True)

        # Normalização de colunas
        df['data_base'] = pd.to_datetime(df['data_base'], format='%Y-%m-%d')
        df['vlr_atbt'] = df['vlr_atbt'].apply(lambda x: Decimal(str(x)) if pd.notnull(x) else Decimal('0'))

        return df
    except Exception as e:
        print(f"Erro ao normalizar o DataFrame: {e}")
        return pd.DataFrame()   
    
    