class Aluno:
    def __init__(self, nome, notas):
        self.nome  = nome
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def verificar_situacao(self):
        media = self.calcular_media()
        if media >= 6.0:
            return "GG pra tu meu mano"
        elif media >= 4.0:
            return "Estuda maix lil bro"
        else:
            return "SF, se deu mal boi"
    


    














































    