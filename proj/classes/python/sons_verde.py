class Instrumento:
    def tocar(self):
        pass


class Violao(Instrumento):
    def tocar(self):
        return "Acorde de violão"


class Flauta(Instrumento):
    def tocar(self):
        return "Melodia doce"   ##menos aura


class Bateria(Instrumento):
    def tocar(self):
        return "Batida forte" ##la ele batida forte


# Lista com instrumentos molestados
instrumentos = [Violao(), Flauta(), Bateria(), Violao(), Bateria()]

# Polimorfismo:tchÊ tchÊ
for instrumento in instrumentos:
    print(instrumento.tocar())








































