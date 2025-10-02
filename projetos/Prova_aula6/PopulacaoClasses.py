import re
import json
from pathlib import Path
import pandas as pd

class DataLoader:
    """Lê e normaliza o Excel para formato longo: municipio, sexo, faixa_etaria, populacao"""
    def __init__(self, path):
        self.path = Path(path)

    def _flatten(self, df):
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = [" ".join([str(p).strip() for p in col if str(p).strip() and str(p).lower()!='nan']).strip()
                          for col in df.columns]
        else:
            df.columns = [str(c).strip() for c in df.columns]
        return df

    def load(self) -> pd.DataFrame:
        try:
            df = pd.read_excel(self.path, header=[0,1], engine='openpyxl')
        except Exception:
            df = pd.read_excel(self.path, header=0, engine='openpyxl')
        df = self._flatten(df)
        df.columns = [str(c).strip() for c in df.columns]
        municipio_col = df.columns[0]
        data_cols = df.columns[1:].tolist()
        if not data_cols:
            raise ValueError("Nenhuma coluna de faixa encontrada.")

        age_re = re.compile(r'\d+\s*a\s*\d+|\d+\s+anos|100 anos|\d+', re.IGNORECASE)
        mapa = {}
        for c in data_cols:
            cs = str(c)
            low = cs.lower()
            sexo = 'Homens' if 'homem' in low else ('Mulheres' if 'mulher' in low else 'Total')
            m = age_re.search(cs)
            faixa = m.group(0).strip() if m else cs.strip()
            mapa[cs] = (sexo, faixa)

        melted = df.melt(id_vars=municipio_col, value_vars=data_cols, var_name='coluna', value_name='populacao')
        melted['coluna'] = melted['coluna'].astype(str)
        melted['sexo'] = melted['coluna'].map(lambda x: mapa.get(x, ('Total', x))[0])
        melted['faixa_etaria'] = melted['coluna'].map(lambda x: mapa.get(x, ('Total', x))[1])

        # normaliza números (milhares e vírgula decimal)
        melted['populacao'] = (melted['populacao'].astype(str)
                              .str.replace(r'\.', '', regex=True)
                              .str.replace(',', '.', regex=False))
        melted['populacao'] = pd.to_numeric(melted['populacao'], errors='coerce')
        melted = melted.dropna(subset=['populacao'])
        melted['populacao'] = melted['populacao'].astype(int)

        long = melted[[municipio_col, 'sexo', 'faixa_etaria', 'populacao']].rename(columns={municipio_col: 'municipio'})
        return long[long['populacao'] > 0].reset_index(drop=True)

class Analyzer:
    """Métodos para responder (a), (b) e (c)"""
    def __init__(self, df_long: pd.DataFrame):
        self.df = df_long.copy()

    def prepare(self):
        # Retorno simples para integração com seu main
        return {'sexo': 'sexo', 'idade': 'faixa_etaria'}

    def find_largest_age_group_by_sex(self, sexo: str):
        sub = self.df[self.df['sexo'].str.lower() == str(sexo).lower()]
        if sub.empty:
            return {'sexo': sexo, 'idade': None, 'populacao': 0}
        agg = sub.groupby('faixa_etaria', as_index=False)['populacao'].sum()
        idx = agg['populacao'].idxmax()
        row = agg.loc[idx]
        return {'sexo': sexo, 'idade': row['faixa_etaria'], 'populacao': int(row['populacao'])}

    def municipality_with_most_for(self, idade: str, sexo: str):
        sub = self.df[(self.df['faixa_etaria'].str.lower() == str(idade).lower()) &
                      (self.df['sexo'].str.lower() == str(sexo).lower())]
        if sub.empty:
            return {'municipio': None, 'populacao': 0}
        agg = sub.groupby('municipio', as_index=False)['populacao'].sum()
        row = agg.loc[agg['populacao'].idxmax()]
        return {'municipio': row['municipio'], 'populacao': int(row['populacao'])}

    def municipality_with_least_for(self, idade: str, sexo: str):
        sub = self.df[(self.df['faixa_etaria'].str.lower() == str(idade).lower()) &
                      (self.df['sexo'].str.lower() == str(sexo).lower())]
        if sub.empty:
            return {'municipio': None, 'populacao': 0}
        agg = sub.groupby('municipio', as_index=False)['populacao'].sum()
        row = agg.loc[agg['populacao'].idxmin()]
        return {'municipio': row['municipio'], 'populacao': int(row['populacao'])}

class OutputWriter:
    """Grava xlsx e json no diretório informado"""
    def __init__(self, out_dir):
        self.out = Path(out_dir)
        self.out.mkdir(parents=True, exist_ok=True)

    def save_json(self, data, filename):
        path = self.out / filename
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return path

    def save_excel(self, df, filename):
        path = self.out / filename
        df.to_excel(path, index=False)
        return path