import mysql.connector

class BancoMySQL:
    def __init__(self, host, user, password, database='puc'):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def criar_tabela(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS vendas (
                id_venda INT PRIMARY KEY,
                produto VARCHAR(100),
                quantidade INT,
                preco_unitario FLOAT,
                data_venda DATE,
                valor_total FLOAT
            )
        """)
        self.conn.commit()

    def inserir_venda(self, venda):
        try:
            self.cursor.execute("""
                INSERT INTO vendas (id_venda, produto, quantidade, preco_unitario, data_venda, valor_total)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    produto=VALUES(produto),
                    quantidade=VALUES(quantidade),
                    preco_unitario=VALUES(preco_unitario),
                    data_venda=VALUES(data_venda),
                    valor_total=VALUES(valor_total)
            """, (venda.id_venda, venda.produto, venda.quantidade, venda.preco_unitario, venda.data_venda, venda.valor_total))
            self.conn.commit()
        except Exception as e:
            print(f"Erro ao inserir venda {venda.id_venda}: {e}")

    def fechar(self):
        self.cursor.close()
        self.conn.close()