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

def balanco_patrimonial(df):
    '''
    Função que aplica as regras de negócio do Capítulo Balanço Patrimonial
    '''
    df = pd.read_csv(
        PATH, 
        sep=",", 
        encoding="utf-8", 
        decimal=".",
        index_col=False,
    )
    colunas = ['nom_atbt', 'nom_arq_orig', 'nom_top', 'nom_agrp', 'nom_cap']
    df[colunas] = df[colunas].astype(str).replace("'", "", regex=True)

    atbts = ['Títulos e Valores Mobiliários', 'Derivativos']
    mask = (df['nom_agrp'] == 'Ativo') & (df['nom_atbt'].isin(atbts))
    df_filtrado = df[mask]

    # Identifica o primeiro 'Títulos e Valores Mobiliários' de cada data_base
    titulos_mask = (df_filtrado['nom_atbt'] == 'Títulos e Valores Mobiliários')
    titulos_primeiro = df_filtrado[titulos_mask & ~df_filtrado.duplicated(['data_base', 'nom_atbt'], keep='first')]

    # Todos os 'Derivativos'
    derivativos = df_filtrado[df_filtrado['nom_atbt'] == 'Derivativos']

    # Soma os valores por data_base
    soma = pd.concat([titulos_primeiro, derivativos]).groupby('data_base', as_index=False)['vlr_atbt'].sum()

    # Preenche os campos do novo registro com base no primeiro 'Títulos e Valores Mobiliários'
    novo_registro = titulos_primeiro.copy()
    novo_registro = novo_registro.drop(columns=['vlr_atbt'])
    novo_registro = novo_registro.merge(soma, on='data_base')
    novo_registro['nom_atbt'] = 'Títulos e Valores Mobiliários e Derivativos'

    # Remove do df original apenas o primeiro 'Títulos e Valores Mobiliários' e todos os 'Derivativos'
    idx_remove = pd.concat([titulos_primeiro, derivativos]).index
    df_final = df.drop(idx_remove).copy()

    # Adiciona o novo registro ao df final
    df_final = pd.concat([df_final, novo_registro], ignore_index=True)

    # Ordena o DataFrame final por data_base e nom_agrp
    df_final = df_final.sort_values(by=['data_base', 'nom_agrp']).reset_index(drop=True)

    return df_final

balanco_patrimonial(
    df=pd.DataFrame()
)


# Segunda opção mais simplificada 

def balanco_patrimonial_simplificado(df):
    '''
    Função que aplica as regras de negócio do Capítulo Balanço Patrimonial
    de forma simplificada
    '''
    df = pd.read_csv(
        PATH, 
        sep=",", 
        encoding="utf-8", 
        decimal=".",
        index_col=False,
    )
    colunas = ['nom_atbt', 'nom_arq_orig', 'nom_top', 'nom_agrp', 'nom_cap']
    df[colunas] = df[colunas].astype(str).replace("'", "", regex=True)

    atbts = ['Títulos e Valores Mobiliários', 'Derivativos']
    mask = (df['nom_agrp'] == 'Ativo') & (df['nom_atbt'].isin(atbts))
    df_filtrado = df[mask]

    # Primeiro 'Títulos e Valores Mobiliários' de cada data_base
    titulos_primeiro = df_filtrado[df_filtrado['nom_atbt'] == 'Títulos e Valores Mobiliários'].drop_duplicates(['data_base', 'nom_atbt'])

    # Todos os 'Derivativos'
    derivativos = df_filtrado[df_filtrado['nom_atbt'] == 'Derivativos']

    # Soma e novo registro
    novo_registro = (
        titulos_primeiro
        .drop(columns=['vlr_atbt'])
        .merge(
            pd.concat([titulos_primeiro, derivativos]).groupby('data_base', as_index=False)['vlr_atbt'].sum(),
            on='data_base'
        )
    )
    novo_registro['nom_atbt'] = 'Títulos e Valores Mobiliários e Derivativos'

    # Remove usados e concatena novo registro
    df_final = pd.concat([df.drop(pd.concat([titulos_primeiro, derivativos]).index), novo_registro], ignore_index=True)

    # Ordena o DataFrame final por data_base e nom_agrp
    df_final = df_final.sort_values(by=['data_base', 'nom_agrp']).reset_index(drop=True)

    return df_final


# Testando a função
def simlificado(df):
    '''
    Função que aplica as regras de negócio do Capítulo Balanço Patrimonial
    de forma simplificada
    '''
    df = pd.read_csv(
        PATH, 
        sep=",", 
        encoding="utf-8", 
        decimal=".",
        index_col=False,
    )
    colunas = ['nom_atbt', 'nom_arq_orig', 'nom_top', 'nom_agrp', 'nom_cap']
    df[colunas] = df[colunas].astype(str).replace("'", "", regex=True)

    atbts = ['Títulos e Valores Mobiliários', 'Derivativos']
    mask = (df['nom_agrp'] == 'Ativo') & (df['nom_atbt'].isin(atbts))
    titulos_primeiro = df[mask & (df['nom_atbt'] == atbts[0])].drop_duplicates(['data_base', 'nom_atbt'])
    derivativos = df[mask & (df['nom_atbt'] == atbts[1])]

    novo_registro = (
        titulos_primeiro.drop(columns=['vlr_atbt'])
        .merge(
            pd.concat([titulos_primeiro, derivativos])
            .groupby('data_base', as_index=False)['vlr_atbt'].sum(),
            on='data_base'
        )
        .assign(nom_atbt='Títulos e Valores Mobiliários e Derivativos')
    )

    df_final = pd.concat(
        [df.drop(pd.concat([titulos_primeiro, derivativos]).index), novo_registro],
        ignore_index=True
    ).sort_values(by=['data_base', 'nom_agrp']).reset_index(drop=True)


    return df_final


def versão_enxuta(df):
    '''
    Função que aplica as regras de negócio do Capítulo Balanço Patrimonial
    de forma enxuta
    '''
    df = pd.read_csv(
        PATH, 
        sep=",", 
        encoding="utf-8", 
        decimal=".",
        index_col=False,
    )
    colunas = ['nom_atbt', 'nom_arq_orig', 'nom_top', 'nom_agrp', 'nom_cap']
    df[colunas] = df[colunas].astype(str).replace("'", "", regex=True)

    a = ['Títulos e Valores Mobiliários', 'Derivativos']
    m = (df['nom_agrp'] == 'Ativo') & (df['nom_atbt'].isin(a))
    t = df[m & (df['nom_atbt'] == a[0])].drop_duplicates(['data_base', 'nom_atbt'])
    d = df[m & (df['nom_atbt'] == a[1])]
    n = t.drop(columns=['vlr_atbt']).merge(pd.concat([t, d])
                                           .groupby('data_base', as_index=False)['vlr_atbt']
                                           .sum(), on='data_base').assign(nom_atbt='Títulos e Valores Mobiliários e Derivativos')
    df_final = pd.concat([df.drop(pd.concat([t, d]).index), n], ignore_index=True
                         ).sort_values(['data_base', 'nom_agrp']
                                       ).reset_index(drop=True)
    
    return df_final



# filtro da soma de forma acertiva

# Filtra registros de interesse
mask = (
    ((df['nom_sub_agrp'] == 'Derivativos') | ((df['nom_atbt'] == 'Derivativos') & (df['nom_agrp'] == 'Ativo')))
)
df_filtrado = df[mask]

# Soma por data_base
resultado = df_filtrado.groupby('data_base', as_index=False)['vlr_atbt'].sum()
resultado = resultado.rename(columns={'vlr_atbt': 'soma_derivativos_ativo'})