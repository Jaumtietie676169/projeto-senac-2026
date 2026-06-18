from datetime import time

from veiculo import Veiculo

class Vaga:

    veiculo: Veiculo
    capacidade: int
    horario_entrada: time
    disponível = True

    def __init__(self, capacidade:int):
        self.capacidade = capacidade