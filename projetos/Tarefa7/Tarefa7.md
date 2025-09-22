# Pipeline de Dados: Vendas

Você foi contratado para criar um pipeline de dados que lê informações de vendas de um arquivo `vendas.csv`, processa os dados e os insere em uma tabela no banco de dados MySQL.

## Regras da atividade

- Criar o arquivo `vendas.csv` com pelo menos 10 registros, contendo as colunas:
  - `id_venda` (inteiro)
  - `produto` (texto)
  - `quantidade` (inteiro)
  - `preco_unitario` (float)
  - `data_venda` (formato YYYY-MM-DD)

## O programa deve

1. Ler o arquivo CSV em Python.
2. Validar os dados (exemplo: quantidade > 0, preço > 0).
3. Calcular o `valor_total = quantidade * preco_unitario`.
4. Conectar ao banco MySQL.
5. Criar a tabela `vendas` se não existir.
6. Inserir os dados no banco.