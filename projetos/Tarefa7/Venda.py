class Venda:
    def __init__(self, id_venda, produto, quantidade, preco_unitario, data_venda):
        self.id_venda = id_venda
        self.produto = produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.data_venda = data_venda
        self.valor_total = self.quantidade * self.preco_unitario

    def validar(self):
        return self.quantidade > 0 and self.preco_unitario > 0