class livro:

    def __init__ (self, quantidade_copias, autor):
        self.quantidade_copias = quantidade_copias
        self.autor = autor

    def vender(self):
        if self.quantidade_copias > 0:
            self.quantidade_copias -= 1
            return True
        return False
    
    def reabastecer(self, quantidade):
        if quantidade > 0:
            self.quantidade_copias += quantidade



















































