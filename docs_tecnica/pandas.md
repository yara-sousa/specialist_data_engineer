# Guia Rapído: Pandas Dataframe

## Pandas (pd.DataFrame)

### Criação
- **pd.DataFrame(data, columns, index, dtype, copy)**
  - Cria DataFrame.
  - `data`: array/dict/list
  - `columns`: nomes colunas
  - `index`: nomes linhas
  - Ex:  
    ```python
    df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    ```

### Leitura
- **pd.read_csv('file.csv', sep=',', header=0, names=None, index_col=None, usecols=None, dtype=None, nrows=None, skiprows=None, encoding=None, na_values=None)**
  - Lê CSV
  - Ex:
    ```python
    df = pd.read_csv('arq.csv')
    ```

### Seleção
- **df['col'] / df.col**
  - Seleciona coluna
- **df[['a', 'b']]**
  - Seleciona várias colunas
- **df.loc[linha, coluna]**
  - Por label
- **df.iloc[linha, coluna]**
  - Por posição
- Ex:
  ```python
  df['A']      # uma coluna
  df.loc[0]    # uma linha
  df.iloc[:, 0] # primeira coluna
  ```

### Filtros
- **df[df['col'] > 2]**
  - Filtra linhas
- Ex:
  ```python
  df[df['A'] > 1]
  ```

### Métodos principais
- **df.head(n) / df.tail(n)**
  - Primeiras/últimas n linhas
- **df.describe()**
  - Estatísticas rápidas
- **df.info()**
  - Resumo tipos/dados
- **df.shape**
  - (linhas, colunas)
- **df.dtypes**
  - Tipos das colunas
- **df.isnull(), df.notnull()**
  - Checa nulos
- **df.fillna(valor), df.dropna()**
  - Preenche/remove nulos
- **df.rename(columns={'a':'b'})**
  - Renomeia colunas
- **df.sort_values('col', ascending=True)**
  - Ordena
- **df.groupby('col').agg({'col2':'sum'})**
  - Agrupa/Agrega
- **df.merge(df2, on='col', how='inner')**
  - Junta DataFrames
- **df.append(df2), df.concat([df,df2], axis=0/1)**
  - Junta linhas/colunas
- **df.apply(func)**
  - Aplica função
- **df['col'].map(func)**
  - Aplica função a coluna
- **df['col'].astype(tipo)**
  - Converte tipo
- **df.drop('col', axis=1)**
  - Remove coluna
- **df.drop(index)**
  - Remove linha
- **df.set_index('col')**
  - Define índice

### Exportação
- **df.to_csv('file.csv', index=False)**
  - Salva em CSV

---

## Link doc oficial 
[documentação pandas](https://pandas.pydata.org/docs/)
