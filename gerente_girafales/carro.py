from .veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, placa:str, peso:float, cor:str, nome_condutor:str):
        super().__init__(placa, peso, cor, nome_condutor, 5)