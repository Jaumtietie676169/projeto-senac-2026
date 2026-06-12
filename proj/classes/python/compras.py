class CarrinhoDeCompras:
    def __init__(self):
        self.itens = []
        self.precos = []

    def adicionar_item(self, nome_produto, preco_produto):
        self.itens.append(nome_produto)
        self.precos.append(preco_produto)

    def calcular_total(self):
        total = 0
        for preco in self.precos:
            total += preco
        return total 
    



















































    