class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.pontuacao = 0

    def acertou_alvo(self, distancia_do_centro):
        if distancia_do_centro < 5:
            self.pontuacao += 100
        elif distancia_do_centro <= 20:
            self.pontuacao += 50
        else:
            self.pontuacao += 10
        return self.pontuacao
    




















































    