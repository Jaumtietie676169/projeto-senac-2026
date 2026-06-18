from .Vaga import Vaga
from .Veiculo import Veiculo
from .erros.VeiculoGrandeException import VeiculoGrandeException
from .erros.VagaIndisponivelException import VagaIndisponivelException


import datetime as dt

class Estacionamento():

    vagas: list[Vaga | None] = [None] * 10


    def __init__(self, vagas: list):
        self.vagas = vagas


    def estacionar(self, veiculo:Veiculo, numero_vaga:int):
        pass

    def estacionar_ajuste_horario(self, veiculo: Veiculo, numero_vaga:int, horario:dt.time):
        pass   

    def verifica_tempo(self, indice:int):
        pass

    def checkout(self, numero_vaga:int):
        pass
