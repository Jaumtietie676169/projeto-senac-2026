class Termometro:
    def __init__(self, temperatura_atual: float):
        self.temperatura_atual = temperatura_atual

    def aumentar(self, graus):
        self.temperatura_atual += graus

    def diminuir(self, graus):
        self.temperatura_atual -= graus

    def alerta_clima(self):
        if self.temperatura_atual < 0:
            return "Cole Palmer"
        elif self.temperatura_atual <= 25:
            return "Dboa pros gurie"
        else:
            return "CR7 GOAT QUENTAÇO"  
        
















































        