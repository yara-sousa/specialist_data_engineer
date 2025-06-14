# Guia Rapído: Spark Dataframe

## PySpark (pyspark.sql.DataFrame)

### Criação
- **spark.createDataFrame(data, schema=None)**
  - Cria DataFrame
- Ex:
  ```python
  df = spark.createDataFrame([(1, 'A'), (2, 'B')], ['id', 'letra'])
  ```

### Leitura
- **spark.read.csv('file.csv', header=True, inferSchema=True, sep=',')**
  - Lê CSV
  - Ex:
    ```python
    df = spark.read.csv('arq.csv', header=True)
    ```

### Seleção
- **df['col']**
  - Seleciona coluna
- **df.select('col1', 'col2')**
  - Seleciona colunas
- **df.filter(df.col > 1) / df.where(...)**
  - Filtro linhas
- Ex:
  ```python
  df.select('id')
  df.filter(df['id'] > 1)
  ```

### Métodos principais
- **df.show(n)**
  - Mostra n linhas
- **df.printSchema()**
  - Mostra schema
- **df.describe()**
  - Estatísticas
- **df.dtypes**
  - Tipos das colunas
- **df.withColumn('nova', expr)**
  - Nova coluna
- **df.drop('col')**
  - Remove coluna
- **df.distinct()**
  - Linhas únicas
- **df.groupBy('col').agg({'col2': 'sum'})**
  - Agrupa/Agrega
- **df.orderBy('col', ascending=True)**
  - Ordena
- **df.join(df2, on='col', how='inner')**
  - Junta DataFrames
- **df.union(df2)**
  - Empilha DataFrames
- **df.na.fill(valor), df.na.drop()**
  - Preenche/Remove nulos
- **df.withColumnRenamed('a', 'b')**
  - Renomeia coluna
- **df.selectExpr("col + 1 as novo")**
  - Expressão SQL

### Exportação
- **df.write.csv('file.csv', header=True)**
  - Salva em CSV

---

## Outros

### Pandas
- **df.pivot(index, columns, values)**
  - Tabela dinâmica
- **df.melt(id_vars, value_vars)**
  - "Desfaz" pivot
- **df.sample(n)**
  - Amostra aleatória

### Spark
- **df.cache()**
  - Mantém em memória
- **df.persist()**
  - Persistência customizada
- **df.repartition(n)**
  - Redivide DataFrame

---

## Link da doc oficial 
[PySpark](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.html