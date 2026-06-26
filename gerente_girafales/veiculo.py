class Veiculo:

    placa: str
    peso: float
    cor: str
    nome_do_condutor: str
    capacidade_passageiros: int

    def __init__(self, placa:str, peso:float, cor:str, nome_condutor:str, capacidade_passageiros:int):
        self.placa = placa
        self.peso = peso
        self.cor = cor
        self.nome_do_condutor = nome_condutor
        self.capacidade_passageiros = capacidade_passageiros