import csv
from Venda import Venda

class LeitorCSV:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo

    def ler_vendas(self):
        vendas = []
        with open(self.caminho_arquivo, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                try:
                    venda = Venda(
                        int(row['id_venda']),
                        row['produto'],
                        int(row['quantidade']),
                        float(row['preco_unitario']),
                        row['data_venda']
                    )
                    if venda.validar():
                        vendas.append(venda)
                except (ValueError, KeyError) as e:
                    print(f"Erro ao processar linha: {row} - {e}")
        return vendas