from veiculo import Veiculo
from onibus import Onibus
from van import Van
from carro import Carro

class VeiculoGrandeException(Exception):
    def __init__(self, mensagem="muito grande meu nego da não!"):
        super().__init__(mensagem)

class VagaIndisponivelException(Exception):
    def __init__(self, mensagem="tem nego ai não chorax não chorax!"):
        super().__init__(mensagem)


class VagaIndisponivelException(Exception):
    def __init__(self, mensagem="tem nego ai não chorax não chorax!"):
        super().__init__(mensagem)


import datetime as dt


class Estacionamento:

    def __init__(self, vagas:list):
        self.vagas = vagas

    def estacionar(self, veiculo: Veiculo, numero_vaga: int):

        if numero_vaga < 0 or numero_vaga >= len(self.vagas):
            raise IndexError("vaga ta bugada p1")

        vaga = self.vagas[numero_vaga]

        if not vaga.disponivel:
            raise VagaIndisponivelException()

        if veiculo.capacidade_passageiros > vaga.capacidade:
            raise VeiculoGrandeException()

        vaga.veiculo = veiculo
        vaga.horario_entrada = dt.datetime.now()
        vaga.disponivel = False

    def estacionar_ajuste_horario(
            self,
            veiculo: Veiculo,
            numero_vaga: int,
            horario: dt.datetime):

        if numero_vaga < 0 or numero_vaga >= len(self.vagas):
            raise IndexError("vaga ta bugada p2")

        vaga = self.vagas[numero_vaga]

        if not vaga.disponivel:
            raise VagaIndisponivelException()

        if veiculo.capacidade_passageiros > vaga.capacidade:
            raise VeiculoGrandeException()

        vaga.veiculo = veiculo
        vaga.horario_entrada = horario
        vaga.disponivel = False

    def verifica_tempo(self, indice: int):

        if indice < 0 or indice >= len(self.vagas):
            raise IndexError("vaga ta bugada p3")

        vaga = self.vagas[indice]

        if vaga.disponivel:
            return 0

        agora = dt.datetime.now()

        diferenca = agora - vaga.horario_entrada

        minutos = diferenca.total_seconds() / 60

        return int(minutos)

    def checkout(self, numero_vaga: int):

        if numero_vaga < 0 or numero_vaga >= len(self.vagas):
            raise IndexError("vaga ta bugada p4")

        vaga = self.vagas[numero_vaga]

        if vaga.disponivel:
            print("tem bagulho nessa vaga não pode ir meu nego.")
            return 0

        minutos = self.verifica_tempo(numero_vaga)

        veiculo = vaga.veiculo

        if isinstance(veiculo, Onibus):
            valor_minuto = 0.10

        elif isinstance(veiculo, Van):
            valor_minuto = 0.09

        else:
            valor_minuto = 0.08

        valor = minutos * valor_minuto

        if minutos < 120:
            valor *= 2

        elif minutos > 600:
            valor *= 0.90

        vaga.veiculo = None
        vaga.horario_entrada = None
        vaga.disponivel = True

        return round(valor, 2)
