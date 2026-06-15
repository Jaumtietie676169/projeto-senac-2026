from veiculo import Veiculo

class Onibus(Veiculo):

    def __init__(self, placa, peso, cor, condutor):
        super().__init__(
            placa,
            peso,
            cor,
            condutor,
            23
        )