from LeitorCSV import LeitorCSV
from BancoMySQL import BancoMySQL

# Configurações do banco
HOST = 'localhost'
USER = 'root'
PASSWORD = ''
DATABASE = 'puc'

# 1. Ler o arquivo CSV
leitor = LeitorCSV('vendas.csv')
vendas = leitor.ler_vendas()

# 2. Conectar ao banco e criar tabela
banco = BancoMySQL(HOST, USER, PASSWORD, DATABASE)
banco.criar_tabela()

# 3. Inserir vendas
for venda in vendas:
    banco.inserir_venda(venda)

banco.fechar()
print("Pipeline finalizado com sucesso!")
